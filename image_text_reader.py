import pytesseract
from PIL import Image
from typing import Tuple
from pathlib import Path

# Define the path to your Tesseract executable (change this if needed)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


# Open the image file
def read_image(path: Path) -> Tuple[str, str]:
    image = Image.open(path)

    # Perform OCR to extract text from the image
    text: str = pytesseract.image_to_string(image)
    return str(path), text
