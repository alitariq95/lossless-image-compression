from PIL import Image, ExifTags
import os


def get_image_metadata(input_path):
    """
    Get the creation and modification dates of the image.

    Args:
        input_path (str): Path to the image file.

    Returns:
        tuple: A tuple containing the creation time and modification time of the image.
    """
    creation_time = os.path.getctime(input_path)  # Get creation time of the image file
    modification_time = os.path.getmtime(input_path)  # Get modification time of the image file
    return creation_time, modification_time


def compress_image(input_path, replace_original_file, quality=95):
    """
    Compress an image file.

    Args:
        input_path (str): Path to the input image file.
        replace_original_file (bool): Whether to replace the original file with the compressed one.
        quality (int): Compression quality (0-100, 100 for best quality).

    Returns:
        bool: True if compression is successful, False otherwise.
    """
    try:
        with Image.open(input_path) as img:
            exif = img.getexif()  # Get EXIF metadata of the image
            creation_time, modification_time = get_image_metadata(input_path)  # Get image metadata

            if exif:
                # Rotate the image if necessary to ensure correct orientation
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = dict(exif)

                if exif.get(orientation) in [3, 6, 8]:
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=True)

            # Remove EXIF metadata
            img = img.convert("RGB")

            # Change the extension to .jpg for the compressed file
            output_path = os.path.splitext(input_path)[0] + "_compressed.jpg"
            print("Compressing image: {}".format(output_path))
            img.save(output_path, quality=quality)  # Save the compressed image

            # Replace the original file with the compressed one if specified
            if replace_original_file:
                print("Deleting original image: {}".format(input_path))
                os.remove(input_path)
                print("Renaming image from: {} to: {}".format(output_path, input_path))
                os.rename(output_path, input_path)

                # Set the preserved metadata (creation and modification dates)
                os.utime(input_path, (creation_time, modification_time))

        return True
    except Exception as e:
        print(f"Error compressing image {input_path}: {e}")
        return False


def compress_images_in_directory(directory, replace_original_file, quality=95):
    """
    Compress all images in a directory.

    Args:
        directory (str): Path to the directory containing images.
        replace_original_file (bool): Whether to replace original files with compressed ones.
        quality (int): Compression quality (0-100, 100 for best quality).
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):  # Check if the file is an image
                file_path = os.path.join(root, file)
                if "compressed" in file_path:
                    print("Image already compressed: {}".format(file_path))
                    continue
                else:
                    compress_image(file_path, replace_original_file, quality=quality)


def main():
    """
    Main function to execute image compression.
    """
    input_directory = input("Enter the path of the directory containing images to compress: ")

    if not os.path.isdir(input_directory):
        print("Invalid directory path.")
        return

    quality = int(input("Enter compression quality (0-100, 100 for best quality): "))

    if quality < 0 or quality > 100:
        print("Invalid quality value. Quality should be between 0 and 100.")
        return

    replace_original_file = input("Replace original file with new file name, Y for Yes and N for No: ")

    if replace_original_file not in ["Y", "N"]:
        print("Invalid response, only Y or No is allowed.")
        return

    replace_original_file = True if replace_original_file == "Y" else False
    compress_images_in_directory(input_directory, replace_original_file, quality=quality)
    print("Image compression completed.")


if __name__ == "__main__":
    main()
