import os
import shutil
from pathlib import Path
from PyPDF2 import PdfMerger, PdfReader
from fpdf import FPDF
import re
import unicodedata


# Define the input and output directories
input_dir = 'input'
output_dir = 'output'
temp_dir = os.path.join(output_dir, 'temp')
output_pdf = os.path.join(output_dir, 'attachments.pdf')
table_of_contents_pdf = os.path.join(output_dir, 'table_of_contents.pdf')
final_output_pdf = os.path.join(output_dir, 'final_output.pdf')

SELECTED_LANGUAGE = 'de'

attachment = {'en': 'Attachment', 'de': 'Anhang'}
page = {'en': 'Page', 'de': 'Seite'}
page_abbr = {'en': 'p.', 'de': 'S.'}
table_of_contents = {'en': 'Table of Contents', 'de': 'Inhaltsverzeichnis'}

attachment_translation = attachment[SELECTED_LANGUAGE]
page_translation = page[SELECTED_LANGUAGE]
page_abbr_translation = page_abbr[SELECTED_LANGUAGE]
table_of_contents_translation = table_of_contents[SELECTED_LANGUAGE]


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


def strip_order_and_extension(filename):
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

    # Remove leading order numbers followed by -, –, or —
    title = re.sub(r'^\s*\d+\s*[-–—]\s*', '', title)

    return title.strip()


def create_title_page(attachment_number, title, attachment_index):
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


def merge_pdfs(input_dir, output_file):
    """Merge PDFs from the input directory into the output file with title pages."""
    merger = PdfMerger()
    title_pages = []
    total_pages = 0
    attachment_number = 1

    filenames = sorted(os.listdir(input_dir))

    if not filenames:
        raise Exception('No PDF files found in the input directory.')

    for filename in filenames:
        if not filename.lower().endswith('.pdf'):
            raise Exception('Have you forgotten non .pdf files in the folder?')

        filepath = os.path.join(input_dir, filename)
        title = strip_order_and_extension(filename)

        print(f"Processing '{filename}' with title '{title}'")

        title_page_pdf = create_title_page(
            f"{attachment_translation} {arabic_to_roman(attachment_number)}",
            title,
            attachment_number
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


def create_table_of_contents_pdf(title_pages, table_of_contents_pdf):
    """Create a table of contents PDF with the list of title pages and their page numbers."""
    pdf = FPDF()
    setup_fonts(pdf)

    pdf.add_page()
    pdf.ln(20)
    pdf.set_right_margin(40)

    pdf.set_font("DocFont", "B", size=20)
    pdf.cell(200, 10, txt=table_of_contents_translation, ln=True, align='C')
    pdf.ln(10)

    pdf.set_left_margin(22)
    pdf.set_font("DocFont", size=12)

    for attachment_number, (title, page_number) in enumerate(title_pages, start=1):
        page_number += 1  # Account for table of contents page

        toc_text = (
            f"{arabic_to_roman(attachment_number)}. "
            f"{title} ({page_abbr_translation} {page_number})"
        )

        pdf.multi_cell(180, 6, txt=toc_text)
        pdf.ln(4)

    pdf.output(table_of_contents_pdf)


def cleanup(directory):
    """Remove temporary directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)


def main():
    # Ensure output and temp directories exist
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # Merge PDFs with title pages
    title_pages = merge_pdfs(input_dir, output_pdf)

    # Create the table_of_contents PDF
    create_table_of_contents_pdf(title_pages, table_of_contents_pdf)

    # Merge the table_of_contents with the final output PDF
    final_merger = PdfMerger()
    final_merger.append(table_of_contents_pdf)
    final_merger.append(output_pdf)
    final_merger.write(final_output_pdf)
    final_merger.close()

    # Cleanup temporary files
    cleanup(temp_dir)

    print(f"PDFs merged successfully into '{final_output_pdf}'.")


if __name__ == '__main__':
    main()
