import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader
from fpdf import FPDF
import re
import unicodedata


"""
# Ghostscript Command
```
gs -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dPDFSETTINGS=/ebook \
  -dNOPAUSE -dQUIET -dBATCH \
  -sOutputFile=compressed.pdf \
  input.pdf
```
Reference Presets

| Preset      | Color images | Grayscale images | Monochrome / 1-bit images | Downsampling enabled? |
| ----------- | -----------: | ---------------: | ------------------------: | --------------------- |
| `/screen`   |       72 dpi |           72 dpi |                   300 dpi | yes                   |
| `/ebook`    |      150 dpi |          150 dpi |                   300 dpi | yes                   |
| `/printer`  |      300 dpi |          300 dpi |                  1200 dpi | no                    |
| `/prepress` |      300 dpi |          300 dpi |                  1200 dpi | no                    |
| `/default`  |       72 dpi |           72 dpi |                   300 dpi | no                    |

### Custom Command

```
gs -sDEVICE=pdfwrite \
  -dCompatibilityLevel=1.4 \
  -dNOPAUSE -dQUIET -dBATCH \
  -dDownsampleColorImages=true \
  -dColorImageResolution=120 \
  -dDownsampleGrayImages=true \
  -dGrayImageResolution=120 \
  -dDownsampleMonoImages=true \
  -dMonoImageResolution=150 \
  -sOutputFile=compressed.pdf \
  input.pdf
```


Compression levels:
    0: default - almost identical to /screen, 72 dpi images
    1: prepress - high quality, color preserving, 300 dpi imgs
    2: printer - high quality, 300 dpi images
    3: ebook - low quality, 150 dpi images
    4: custom - /ebook with 110 dpi images, between ebook and screen
    5: custom - /ebook with 90 dpi images, between level 4 and screen
    6: screen - screen-view-only quality, 72 dpi images

"""

def ebook_with_dpi(dpi):
    """Ghostscript options for the /ebook preset with color and grayscale images downsampled to dpi."""
    return ['-dPDFSETTINGS=/ebook', f'-dColorImageResolution={dpi}', f'-dGrayImageResolution={dpi}']


# Ghostscript options for each compression level
COMPRESSION_PRESETS = {
    0: ['-dPDFSETTINGS=/default'],
    1: ['-dPDFSETTINGS=/prepress'],
    2: ['-dPDFSETTINGS=/printer'],
    3: ['-dPDFSETTINGS=/ebook'],
    # Custom levels between /ebook (150 dpi) and /screen (72 dpi)
    4: ebook_with_dpi(110),
    5: ebook_with_dpi(90),
    6: ['-dPDFSETTINGS=/screen'],
}

attachment = {'en': 'Attachment', 'de': 'Anhang'}
page = {'en': 'Page', 'de': 'Seite'}
page_abbr = {'en': 'p.', 'de': 'S.'}
table_of_contents = {'en': 'Table of Contents', 'de': 'Inhaltsverzeichnis'}


FONT_REGULAR = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")


def setup_fonts(pdf):
    if not FONT_REGULAR.exists():
        raise FileNotFoundError(f"Font not found: {FONT_REGULAR}")

    # Register regular font
    pdf.add_font("DocFont", "", str(FONT_REGULAR))

    # Register bold font if available, otherwise reuse regular font
    if FONT_BOLD.exists():
        pdf.add_font("DocFont", "B", str(FONT_BOLD))
    else:
        pdf.add_font("DocFont", "B", str(FONT_REGULAR))


def arabic_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_num = ''
    i = 0

    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1

    return roman_num


def strip_order_and_extension(filename, remove_order_suffix=False):
    """
    Examples:
    '00 – Eheurkunde – Nachweis über die Namensänderung.pdf'
    -> 'Eheurkunde – Nachweis über die Namensänderung'

    '11 – Arbeitszeugnis SAP SE: 1 Assesment Form und 2 Reference Letters.pdf'
    -> 'Arbeitszeugnis SAP SE: 1 Assesment Form und 2 Reference Letters'
    """

    title = Path(filename).stem

    # Normalize macOS filename Unicode:
    # "u" + combining diaeresis -> "ü"
    title = unicodedata.normalize("NFC", title)

    if not remove_order_suffix:
        return title.strip()

    # Remove leading order numbers followed by -, –, or —
    title = re.sub(r'^\s*\d+\s*[-–—]\s*', '', title)

    return title.strip()


def create_title_page(attachment_number, title, attachment_index, temp_dir):
    """Generate a title page PDF with the given attachment number and title."""
    pdf = FPDF()
    setup_fonts(pdf)

    pdf.add_page()
    pdf.set_y(100)

    pdf.set_font("DocFont", size=16)
    pdf.cell(0, 10, txt=attachment_number, ln=True, align='C')

    pdf.set_font("DocFont", "B", size=20)
    pdf.multi_cell(0, 10, txt=title, align='C')

    # Do not use title in temp filename because it may contain characters like / or :
    title_pdf = os.path.join(temp_dir, f'title_page_{attachment_index}.pdf')
    pdf.output(title_pdf)

    return title_pdf


def merge_pdfs(input_dir, output_file, temp_dir, language, reverse_order: bool = True, remove_order_suffix: bool = True):
    """Merge PDFs from the input directory into the output file with title pages."""
    merger = PdfMerger()
    title_pages = []
    total_pages = 0
    attachment_number = 1

    # Skip subdirectories (e.g. the output directory when running with -i .) and hidden files like .DS_Store
    filenames = [
        filename for filename in os.listdir(input_dir)
        if not filename.startswith('.') and os.path.isfile(os.path.join(input_dir, filename))
    ]

    # Sort in reverse order to match the original script's behavior
    filenames = sorted(filenames, reverse=reverse_order)

    if not filenames:
        raise Exception('No PDF files found in the input directory.')

    for filename in filenames:
        if not filename.lower().endswith('.pdf'):
            raise Exception('Have you forgotten non .pdf files in the folder?')

        filepath = os.path.join(input_dir, filename)
        title = strip_order_and_extension(
            filename, remove_order_suffix=remove_order_suffix)

        print(f"Processing '{filename}' with title '{title}'")

        title_page_pdf = create_title_page(
            f"{attachment[language]} {arabic_to_roman(attachment_number)}",
            title,
            attachment_number,
            temp_dir
        )

        title_pages.append((title, total_pages + 1))

        merger.append(title_page_pdf)
        merger.append(filepath)

        total_pages += len(PdfReader(title_page_pdf).pages)
        total_pages += len(PdfReader(filepath).pages)

        attachment_number += 1

    merger.write(output_file)
    merger.close()

    return title_pages


def create_table_of_contents_pdf(title_pages, table_of_contents_pdf, language):
    """Create a table of contents PDF with the list of title pages and their page numbers."""
    pdf = FPDF()
    setup_fonts(pdf)

    pdf.add_page()
    pdf.ln(20)
    pdf.set_right_margin(40)

    pdf.set_font("DocFont", "B", size=20)
    pdf.cell(200, 10, txt=table_of_contents[language], ln=True, align='C')
    pdf.ln(10)

    pdf.set_left_margin(22)
    pdf.set_font("DocFont", size=12)

    for attachment_number, (title, page_number) in enumerate(title_pages, start=1):
        page_number += 1  # Account for table of contents page

        toc_text = (
            f"{arabic_to_roman(attachment_number)}. "
            f"{title} ({page_abbr[language]} {page_number})"
        )

        pdf.multi_cell(180, 6, txt=toc_text)
        pdf.ln(4)

    pdf.output(table_of_contents_pdf)


def cleanup(directory):
    """Remove temporary directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)


def compress_pdf(input_file, output_file, level=None, dpi=None, mono_dpi=150):
    """Compress a PDF with Ghostscript, using either a preset (level) or custom image resolutions (dpi)."""
    gs = shutil.which('gs')
    if gs is None:
        raise FileNotFoundError("Ghostscript not found. On macOS install it via 'brew install ghostscript'.")

    if level is not None:
        image_settings = COMPRESSION_PRESETS[level]
    else:
        image_settings = [
            '-dDownsampleColorImages=true',
            f'-dColorImageResolution={dpi}',
            '-dDownsampleGrayImages=true',
            f'-dGrayImageResolution={dpi}',
            '-dDownsampleMonoImages=true',
            f'-dMonoImageResolution={mono_dpi}',
        ]

    print(f"Compressing '{input_file}' with Ghostscript...")

    # Blocks until Ghostscript has finished; raises CalledProcessError if it fails
    subprocess.run(
        [
            gs,
            '-sDEVICE=pdfwrite',
            '-dCompatibilityLevel=1.4',
            *image_settings,
            '-dNOPAUSE', '-dQUIET', '-dBATCH',
            # Ghostscript reads '%' in the output filename as a page number format, '%%' is a literal '%'
            f'-sOutputFile={output_file.replace("%", "%%")}',
            input_file,
        ],
        check=True,
    )

    original_size = os.path.getsize(input_file) / 1e6
    compressed_size = os.path.getsize(output_file) / 1e6
    print(f"PDF compressed into '{output_file}' ({original_size:.2f} MB -> {compressed_size:.2f} MB).")


def output_filename(value):
    """Argparse type for --output-name: strips an optional .pdf extension and rejects directories."""
    name = value[:-len('.pdf')] if value.lower().endswith('.pdf') else value
    if not name:
        raise argparse.ArgumentTypeError('the filename must not be empty')
    if os.path.basename(name) != name:
        raise argparse.ArgumentTypeError(f"'{value}' contains a directory, use --output-dir for that")
    return name


def parse_args():
    parser = argparse.ArgumentParser(
        description='Merge all PDFs of a directory into one PDF with a table of contents '
                    'and a title page before each attachment.')
    parser.add_argument('-i', '--input-dir', default='input',
                        help='directory with the PDFs to merge (default: %(default)s)')
    parser.add_argument('-o', '--output-dir', default='output',
                        help='directory for the generated PDFs (default: %(default)s)')
    parser.add_argument('-n', '--output-name', type=output_filename, default='final_output', metavar='NAME',
                        help='filename of the final PDF, the extension stays .pdf (default: %(default)s)')
    parser.add_argument('-l', '--language', choices=['de', 'en'], default='de',
                        help='language of the title pages and the table of contents (default: %(default)s)')
    parser.add_argument('--reverse-order', action=argparse.BooleanOptionalAction, default=True,
                        help='sort the PDFs by filename in descending order')
    parser.add_argument('--remove-order-prefix', action='store_true',
                        help="remove leading order numbers like '00 – ' from the titles")

    compression = parser.add_argument_group(
        'compression',
        "Additionally write a compressed copy of the final PDF (NAME_compressed.pdf) "
        "with Ghostscript (brew install ghostscript).")
    compression_mode = compression.add_mutually_exclusive_group()
    compression_mode.add_argument('-c', '--compress', type=int, choices=COMPRESSION_PRESETS, metavar='LEVEL',
                                  help='compress with a preset: '
                                       '0=/default, 1=/prepress, 2=/printer, 3=/ebook, '
                                       '4=/ebook at 110 dpi, 5=/ebook at 90 dpi, 6=/screen')
    compression_mode.add_argument('--dpi', type=int,
                                  help='compress by downsampling color and grayscale images to DPI')
    compression.add_argument('--mono-dpi', type=int, default=150,
                             help='resolution for monochrome images when using --dpi (default: %(default)s)')

    # argparse accepts values glued to short options and would read '-output-dir' as '-o utput-dir',
    # so short options must be a single letter, separated from their value by a space
    for arg in sys.argv[1:]:
        if re.match(r'-[a-zA-Z].', arg):
            parser.error(f"invalid argument '{arg}': short options need a space before their value "
                         "(e.g. '-o DIR'), long options need two dashes (e.g. '--output-dir')")

    args = parser.parse_args()

    # Validate before any directory is created, relative paths start from the current directory
    if not os.path.isdir(args.input_dir):
        parser.error(f"input directory '{os.path.abspath(args.input_dir)}' not found (set it with -i)")
    # Otherwise the generated PDFs would be merged as attachments in the next run
    if os.path.isdir(args.output_dir) and os.path.samefile(args.input_dir, args.output_dir):
        parser.error('the output directory must differ from the input directory')

    return args


def main():
    args = parse_args()

    output_dir = args.output_dir
    temp_dir = os.path.join(output_dir, 'temp')
    output_pdf = os.path.join(output_dir, 'attachments.pdf')
    table_of_contents_pdf = os.path.join(output_dir, 'table_of_contents.pdf')
    final_output_pdf = os.path.join(output_dir, f'{args.output_name}.pdf')
    compressed_output_pdf = os.path.join(output_dir, f'{args.output_name}_compressed.pdf')

    # Ensure output and temp directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Merge PDFs with title pages
    title_pages = merge_pdfs(args.input_dir, output_pdf, temp_dir, args.language,
                             reverse_order=args.reverse_order,
                             remove_order_suffix=args.remove_order_prefix)

    # Create the table_of_contents PDF
    create_table_of_contents_pdf(title_pages, table_of_contents_pdf, args.language)

    # Merge the table_of_contents with the final output PDF
    final_merger = PdfMerger()
    final_merger.append(table_of_contents_pdf)
    final_merger.append(output_pdf)
    final_merger.write(final_output_pdf)
    final_merger.close()

    # Cleanup temporary files
    cleanup(temp_dir)

    print(f"PDFs merged successfully into '{final_output_pdf}'.")

    # Compress the final output PDF with Ghostscript
    if args.compress is not None or args.dpi is not None:
        compress_pdf(final_output_pdf, compressed_output_pdf,
                     level=args.compress, dpi=args.dpi, mono_dpi=args.mono_dpi)


if __name__ == '__main__':
    main()
