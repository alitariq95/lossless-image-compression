# Lossless Image Compression

This project provides a simple Python script for lossless compression of images in a specified directory while preserving metadata. It utilizes the Pillow library for image processing and relies on Python 3.9 or higher.

## How to Run

1. Ensure you have Python 3.9 installed on your system. If not, you can download and install it from the official Python website: [Python Downloads](https://www.python.org/downloads/).
2. Clone or download the project repository to your local machine.
3. Navigate to the project directory using the command line or terminal.
4. Install the required dependencies by running the following command: `pip3 install -r requirements.txt`
5. Once the dependencies are installed, you can run the project by executing the main script `main.py` with Python 3.9. Use the following command:
`python main.py`
6. Follow the on-screen prompts to provide the path to the directory containing images you want to compress, specify the compression quality, and choose whether to replace original files with compressed ones.
7. The script will process the images in the specified directory, compress them, and provide feedback on the compression process.
8. After completion, you will receive a message indicating that the image compression is completed.

## Additional Information

- The script supports various image formats such as PNG, JPEG, JPG, and BMP.
- It preserves the creation and modification dates of the original images.
- Image orientation is corrected automatically based on EXIF metadata.
- You can adjust the compression quality from 0 to 100, where 100 indicates the best quality.
- Original files can be replaced with the compressed ones or kept separately based on user preference.

Feel free to explore and modify the script according to your requirements!
