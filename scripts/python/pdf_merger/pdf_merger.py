import os
from PyPDF2 import PdfMerger

# directory with pdf files to merge
pdfs_dir = './pdfs_to_merge'

# Output directory
output_dir = './output'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# get all pdf files in the directory
pdfs = [os.path.join(pdfs_dir, f)
        for f in os.listdir(pdfs_dir) if f.endswith('.pdf')]
pdfs.sort()


merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

# Output file path
output_file_path = os.path.join(output_dir, "Merged-File.pdf")

merger.write(output_file_path)
merger.close()
