import PyPDF2
import uuid


def extract_pdf_pages(pdf_filename, ranges):
    with open(pdf_filename, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for range_ in ranges:
            start_page, end_page = range_
            if start_page < 1 or end_page > len(reader.pages):
                print(f"Invalid range {start_page}-{end_page}. Skipping.")
                continue

            writer = PyPDF2.PdfWriter()
            for page_num in range(start_page - 1, end_page):
                page = reader.pages[page_num]
                writer.add_page(page)

            unique_filename = f"output/extracted_pdf_{start_page}_{end_page}_{uuid.uuid4().hex}.pdf"
            with open(unique_filename, 'wb') as new_pdf:
                writer.write(new_pdf)

            print(
                f"Extracted pages {start_page}-{end_page} to {unique_filename}")


if __name__ == "__main__":
    # Replace this with your PDF file name
    pdf_filename = "input/projektarbeit.pdf"
    ranges = [
        [28, 42],  # This will extract pages 1 to 3
        [43, 49],  # This will extract pages 5 to 7
        # Add more ranges as needed
    ]

    extract_pdf_pages(pdf_filename, ranges)
