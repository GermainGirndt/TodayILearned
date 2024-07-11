import os
from PyPDF2 import PdfMerger, PdfReader
from fpdf import FPDF

# Define the input and output directories
input_dir = 'input'
output_dir = 'output'
output_pdf = os.path.join(output_dir, 'output.pdf')
summary_pdf = os.path.join(output_dir, 'summary.pdf')
final_output_pdf = os.path.join(output_dir, 'final_output.pdf')


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
    pdf.set_font("times", size=18)
    pdf.cell(0, 10, txt=attachment_number, ln=True, align='C')

    pdf.set_font("times", size=24)
    pdf.multi_cell(0, 10, txt=title, align='C')
    title_pdf = os.path.join(output_dir, f'{attachment_number}_{title}.pdf')
    pdf.output(title_pdf)
    return title_pdf


def sanitize_filename(filename):
    """Sanitize filename to create a title."""
    return ''.join(c for c in filename.replace('.pdf', '') if c.isalnum() or c.isspace())


def merge_pdfs(input_dir, output_file):
    """Merge PDFs from the input directory into the output file with title pages."""
    merger = PdfMerger()
    title_pages = []
    total_pages = 0

    attachment_number = 1
    for filename in sorted(os.listdir(input_dir)):
        if filename.endswith('.pdf'):
            filepath = os.path.join(input_dir, filename)
            title = sanitize_filename(filename)

            # Create title page
            title_page_pdf = create_title_page(
                f"Attachment {arabic_to_roman(attachment_number)}", title)
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


def create_summary_pdf(title_pages, summary_pdf):
    """Create a summary PDF with the list of title pages and their page numbers."""
    summary = FPDF()
    summary.add_page()
    summary.set_font("times", size=20)
    summary.cell(200, 10, txt="Summary", ln=True, align='C')
    summary.ln(10)

    summary.set_font("times", size=12)
    for attachment_number, (title, page_number) in enumerate(title_pages, start=1):
        page_number += 1  # Account for this summary page
        summary_text = f"Attachment {arabic_to_roman(attachment_number)} - {title} (PDF Page {page_number})"
        summary.cell(200, 10, txt=summary_text, ln=True)

    summary.output(summary_pdf)


def cleanup(files):
    """Remove temporary files."""
    for file in files:
        os.remove(file)


def main():
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Merge PDFs with title pages
    title_pages = merge_pdfs(input_dir, output_pdf)

    # Create the summary PDF
    create_summary_pdf(title_pages, summary_pdf)

    # Merge the summary with the final output PDF
    final_merger = PdfMerger()
    final_merger.append(summary_pdf)
    final_merger.append(output_pdf)
    final_merger.write(final_output_pdf)
    final_merger.close()

    print(f"PDFs merged successfully into '{final_output_pdf}'.")


if __name__ == '__main__':
    main()
