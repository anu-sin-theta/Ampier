# Project Ampier 

### Project Goal

The goal of this project is to provide small businesses with their own Natural Language Processing (NLP) model for customer interaction. Ampier uses Python and several libraries to process and tokenize text from various file formats, including PDFs, CSVs, Excel files, text files, and images. The tokenized text can then be used to train an NLP model.

### Libraries Used

- `transformers`: This library provides thousands of pretrained models to perform tasks on texts such as classification, information extraction, and more.
- `PyPDF2`: A library capable of splitting, merging and transforming the pages of PDF files.
- `pandas`: A library providing high-performance, easy-to-use data structures and data analysis tools.
- `PIL`: Python Imaging Library is used for opening, manipulating, and saving many different image file formats.
- `pytesseract`: An optical character recognition (OCR) tool for Python that recognizes and reads the text embedded in images.

### Installation

Before running the script, you need to install the necessary libraries. You can do this by running the following commands in your terminal:

For Linux, you also need to install Tesseract via your package manager:

and on windows install Tesseract.exe and provide the path in the program.

### How to Use

The main function of the script is `preprocess_text(text)`, which takes a string of text as input and returns a list of tokens. The text is tokenized using the `AutoTokenizer` class from the transformers library.

The script can handle various file formats:

- For PDF files, the script reads the text from each page of the PDF.
- For CSV and Excel files, the script reads the data and converts it into a string.
- For text files, the script reads the text directly from the file.
- For image files, the script uses OCR to extract text from the image.

To use the script, you need to provide the path to the file you want to tokenize. The script will then read the file, preprocess the text, and print the tokens. The tokens are also stored in a file named 'tokens.txt'.

### Code

The main code of the project is in the `textmachine.py` file. The code is well-commented and should be easy to understand. If you have any questions or issues, feel free to ask.

### Future Work

In the future, we plan to add more features to the script, such as support for more file formats and the ability to train an NLP model directly from the script. Stay tuned for updates!
