from pdf2image import convert_from_path
from pathlib import Path


def pdf_to_image_converter(pdf_path: Path) -> bool:
    pdf_file = pdf_path

    images: list = convert_from_path(pdf_file)

    for i, image in enumerate(images):
        image.save(f'output_images/output_page_{i + 1}.jpg', 'JPEG')
    return True
