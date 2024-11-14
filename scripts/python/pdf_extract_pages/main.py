import PyPDF2
from PyPDF2 import PdfMerger
import uuid


def extract_pdf_pages(pdf_filename, ranges, merge: bool = False):

    filenames = []

    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for range_ in ranges:
            start_page, end_page = range_
            if start_page < 1 or end_page > len(reader.pages) or end_page < -1:
                print(f"Invalid range {start_page}-{end_page}. Skipping.")
                continue

            if end_page == -1:
                end_page = len(reader.pages)

            writer = PyPDF2.PdfWriter()
            for page_num in range(start_page - 1, end_page):
                page = reader.pages[page_num]
                writer.add_page(page)

            unique_filename = f"output/extracted_pdf_{start_page}_{end_page}_{uuid.uuid4().hex}.pdf"
            with open(unique_filename, 'wb') as new_pdf:
                writer.write(new_pdf)

            print(
                f"Extracted pages {start_page}-{end_page} to {unique_filename}")
            filenames.append(unique_filename)

    if merge:
        merger = PdfMerger()
        for filename in filenames:
            merger.append(filename)

        merged_filename = f"output/merged_extracted_pdf_{uuid.uuid4().hex}.pdf"
        merger.write(merged_filename)
        merger.close()

        print(f"Merged all extracted PDFs into {merged_filename}")


if __name__ == "__main__":
    # Replace this with your PDF file name
    pdf_filename = "input/2023- Recibo e Declaracao Imposto de Renda - Rodrigo - Exercicio 2023 - Calendario 2022.pdf"
    ranges = [
        [1, 1],  # This will extract pages 1 to 10
        [3, -1]  # Add more ranges as needed
    ]

    extract_pdf_pages(
        pdf_filename=pdf_filename,
        ranges=ranges,
        merge=True
    )
