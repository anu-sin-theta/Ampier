from transformers import AutoTokenizer, pipeline
import PyPDF2
import pandas as pd
from PIL import Image
import pytesseract



def handle_input_file(file_path):
    if file_path.endswith('.pdf'):
        return handle_pdf(file_path)
    elif file_path.endswith('.csv') or file_path.endswith('.xlsx'):
        return handle_csv_excel(file_path)
    elif file_path.endswith(('.png', '.jpg', '.jpeg')):
        return handle_image_file(file_path)
    elif file_path.endswith('.txt'):
         return handle_text_file(file_path)
    else:
        print("File format not supported")


def handle_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

def handle_csv_excel(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    return df.to_string()

def handle_text_file(file_path):
    file = open(file_path, 'r')
    text = file.read()
    file.close()
    return text

def handle_image_file(file_path):
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    return text

def preprocess_text(text):
    text = str(text)
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    tokens = tokenizer.tokenize(text)
    return tokens

# file_path = input("Enter the file path: ")
text = handle_input_file("test.png") #ye bass test ke liye hai
tokens = preprocess_text(text)
print(tokens)
# store the tokens in a file
file = open('tokens.txt', 'w')
file.write(str(tokens))
file.close()