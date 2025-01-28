import fitz  # PyMuPDF
import os
from PIL import Image
import io

# Define paths
input_dir = os.path.join(os.getcwd(), "input")
output_dir = os.path.join(os.getcwd(), "output")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define image compression parameters
image_quality = 70  # Adjustable: lower values reduce quality and file size
image_dpi = 100     # Adjustable DPI; reduces resolution

# Loop through all files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.lower().endswith(".pdf"):  # Process only PDF files
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        # Open PDF
        with fitz.open(input_path) as pdf:
            # Iterate over each page
            for page_num in range(pdf.page_count):
                page = pdf[page_num]
                # Get all images on the page
                for img_index, img in enumerate(page.get_images(full=True)):
                    xref = img[0]
                    # Extract image
                    base_image = pdf.extract_image(xref)
                    image_data = base_image["image"]

                    # Open image with PIL and apply quality settings
                    image = Image.open(io.BytesIO(image_data))
                    image = image.convert("RGB")  # Ensure RGB format for PIL
                    temp_image = io.BytesIO()

                    # Save image with reduced quality
                    image.save(temp_image, format="JPEG",
                               quality=image_quality, dpi=(image_dpi, image_dpi))

                    # Replace the original image with the optimized one
                    pdf.replace_image(xref, temp_image.getvalue())

            # Save the compressed PDF with additional optimization
            pdf.save(output_path, garbage=4, deflate=True, clean=True)

        print(f"Compressed and saved: {output_path}")

print("All PDF files have been compressed and saved in the output directory.")
