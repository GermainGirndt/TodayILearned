# install HEIF library
# brew install libheif
# PIP INSTALL PILLOW

import os
from PIL import Image
import subprocess


def convert_heic_to_jpg(input_folder_path, output_folder_path):
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".HEIC") or filename.endswith(".heic"):
            heic_path = os.path.join(input_folder_path, filename)
            jpg_path = os.path.join(output_folder_path, filename)

            try:
                subprocess.run(["sips", "-s", "format", "jpeg",
                               heic_path, "--out", jpg_path])
                print(f"Converted {heic_path} to {jpg_path}")
            except Exception as e:
                print(f"Error converting {heic_path}: {str(e)}")


# Example usage
# Replace with the path to your folder containing .HEIC images
input_folder_path = './input'
output_folder_path = './output'
convert_heic_to_jpg(input_folder_path, output_folder_path)
