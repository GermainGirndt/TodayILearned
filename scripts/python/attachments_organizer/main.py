import os
import shutil
from PyPDF2 import PdfMerger, PdfReader
from fpdf import FPDF
import re

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


def create_title_page(attachment_number, title):
    """Generate a title page PDF with the given attachment number and title."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_y(100)
    pdf.set_font("times", size=16)
    pdf.cell(0, 10, txt=attachment_number, ln=True, align='C')

    pdf.set_font("times", "B", size=20)
    pdf.multi_cell(0, 10, txt=title, align='C')
    title_pdf = os.path.join(temp_dir, f'{attachment_number}_{title}.pdf')
    pdf.output(title_pdf)
    return title_pdf


def sanitize_filename(filename):
    """Sanitize filename to create a title."""

    pattern = r'[0-9]+\s\-\s.*'

    if re.match(pattern, filename):
        # Remove the attachment number and the dash
        filename = re.sub(r'[0-9]+\s\-\s', '', filename)

    return ''.join(c for c in filename.replace('.pdf', '') if c.isalnum() or c.isspace() or c in ['-'])


def merge_pdfs(input_dir, output_file):
    """Merge PDFs from the input directory into the output file with title pages."""
    merger = PdfMerger()
    title_pages = []
    total_pages = 0

    attachment_number = 1
    for filename in sorted(os.listdir(input_dir)):
        if not filename.endswith('.pdf'):
            raise Exception('Have you forgotten non .pdf files in the folder?')
        filepath = os.path.join(input_dir, filename)
        title = sanitize_filename(filename)

        # Create title page
        title_page_pdf = create_title_page(
            f"{attachment_translation} {arabic_to_roman(attachment_number)}", title)
        title_pages.append((title, total_pages + 1))

        # Merge the title page and the document
        merger.append(title_page_pdf)
        merger.append(filepath)

        # Update the total number of pages
        total_pages += len(PdfReader(title_page_pdf).pages)
        total_pages += len(PdfReader(filepath).pages)

        attachment_number += 1

    merger.write(output_file)
    merger.close()

    return title_pages


def create_table_of_contents_pdf(title_pages, table_of_contents_pdf):
    """Create a table_of_contents PDF with the list of title pages and their page numbers."""
    table_of_contents = FPDF()
    table_of_contents.add_page()
    table_of_contents.ln(20)
    table_of_contents.set_right_margin(40)
    table_of_contents.set_font("times", "B", size=20)
    table_of_contents.cell(
        200, 10, txt=table_of_contents_translation, ln=True, align='C')
    table_of_contents.ln(10)

    table_of_contents.set_left_margin(22)
    table_of_contents.set_font("times", size=12)
    for attachment_number, (title, page_number) in enumerate(title_pages, start=1):
        page_number += 1  # Account for this table_of_contents page
        table_of_contents_text = f"{arabic_to_roman(attachment_number)}. {title} ({page_abbr_translation} {page_number})"
        table_of_contents.multi_cell(
            180, 6, txt=table_of_contents_text, ln=True)
        table_of_contents.ln(4)

    table_of_contents.output(table_of_contents_pdf)


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
