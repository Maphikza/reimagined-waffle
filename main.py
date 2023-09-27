from pdf_to_images_converter import pdf_to_image_converter
from image_text_reader import read_image
from pathlib import Path

IMAGES_DIRECTORY = Path("output_images")


# Define a custom sorting key function to extract the numeric part of filenames
def get_numeric_part(filename):
    return int(filename.stem.split('_')[-1])


def clean_out_directory(dir_path: Path) -> bool:
    for item in dir_path.iterdir():
        if item.is_file():
            item.unlink()
    return True


if __name__ == "__main__":
    pasted_path = Path(input("Supply the path to the pdf document that you would like to extract text from.\n-"))
    if pasted_path.is_file() and str(pasted_path).endswith('.pdf') and not pasted_path.is_dir():
        chosen_path = pasted_path
        pdf_path = pasted_path
        contents = list(IMAGES_DIRECTORY.iterdir())
        sorted_contents = sorted(contents, key=get_numeric_part)
        text_file_path = Path("output_text.txt")

        if not contents:
            converted = pdf_to_image_converter(pdf_path)
            if converted:
                contents = list(IMAGES_DIRECTORY.iterdir())
                sorted_contents = sorted(contents, key=get_numeric_part)
                for image in sorted_contents:
                    info, extracted_text = read_image(Path(image))
                    # print(f"{extracted_text}\n\n-------\n")
                    with open(text_file_path, 'a') as file:
                        file.write(extracted_text.strip() + '\n')
                cleaned_up = clean_out_directory(IMAGES_DIRECTORY)
                if cleaned_up:
                    print("The directory has been emptied out.")
        else:
            for image in sorted_contents:
                info, extracted_text = read_image(Path(image))
                print(f"{extracted_text}\n\n-------\n")
            cleaned_up = clean_out_directory(IMAGES_DIRECTORY)
            if cleaned_up:
                print("The directory has been emptied out.")
    else:
        print("The path you have provided is either a directory or an invalid path.")
