import PyPDF2
import os
from PyPDF2 import PdfMerger


def remove_pages_from_pdf(pages_to_remove):

    # directory with pdf files to merge
    input_dir = './input'
    # Output directory
    output_dir = './output'

    if pages_to_remove is None or len(pages_to_remove) == 0:
        raise Exception("No pages to remove")

    # Create output directory if it doesn't exist
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # get all pdf files in the directory
    pdfs = [os.path.join(input_dir, f)
            for f in os.listdir(input_dir) if f.endswith('.pdf')]

    if len(pdfs) != 1:
        raise Exception(
            f"There should be exactly one pdf file in the directory. Found: {len(pdfs)} ")

    pdf = pdfs[0]

    output_pdf = os.path.join(output_dir, "output.pdf")

    # Read the source PDF file
    input_pdf_file = PyPDF2.PdfReader(pdf)

    # Create a new PDF file writer object
    output_pdf_file = PyPDF2.PdfWriter()

    # Iterate over all pages in the source PDF
    for page_number in range(len(input_pdf_file.pages)):
        # If the page number is not in the list of pages to remove, add it to the new PDF
        if page_number + 1 not in pages_to_remove:
            output_pdf_file.add_page(input_pdf_file.pages[page_number])

    # Write the output PDF to a file
    with open(output_pdf, "wb") as output_pdf_handle:
        output_pdf_file.write(output_pdf_handle)

    print("PDF page removal complete!")


# List of pages to remove (0-indexed)
pages_to_remove = [2]
remove_pages_from_pdf(pages_to_remove)
