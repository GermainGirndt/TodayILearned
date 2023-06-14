# install HEIF library
# brew install libheif

import os
from PIL import Image
import pyheif_pillow_opener
import subprocess


def convert_heic_to_jpg(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".HEIC") or filename.endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpg_path = os.path.splitext(heic_path)[0] + ".jpg"

            try:
                subprocess.run(["sips", "-s", "format", "jpeg", heic_path, "--out", jpg_path])
                print(f"Converted {heic_path} to {jpg_path}")
            except Exception as e:
                print(f"Error converting {heic_path}: {str(e)}")


# Example usage
folder_path = '/Users/germaingirndt/Downloads/Fotos Modem'  # Replace with the path to your folder containing .HEIC images
convert_heic_to_jpg(folder_path)
