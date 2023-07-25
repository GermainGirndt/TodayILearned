import os
import PyPDF2


def compress_pdf(pdf_path, output_path):
    # Creating pdf file reader object
    pdf_file_obj = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

    # Creating pdf writer object for new pdf
    pdf_writer = PyPDF2.PdfWriter()

    # Copying the pages from the original pdf to the new one.
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Writing out the new pdf
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

    pdf_file_obj.close()


def find_and_compress_pdf(input_dir, output_dir):
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]

    if len(pdf_files) != 1:
        print(
            f"Error: Expected exactly one .pdf file in {input_dir}, but found {len(pdf_files)}.")
        return

    pdf_file = pdf_files[0]
    compress_pdf(os.path.join(input_dir, pdf_file),
                 os.path.join(output_dir, pdf_file))


if __name__ == "__main__":
    find_and_compress_pdf('input', 'output')
