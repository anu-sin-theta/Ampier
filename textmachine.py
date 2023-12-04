import PyPDF2
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')


def handle_input_file(file_path):
    if file_path.endswith('.pdf'):
        return handle_pdf(file_path)
    elif file_path.endswith('.csv') or file_path.endswith('.xlsx'):
        return handle_csv_excel(file_path)
    else:
        return "Unsupported file type"


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


def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [i for i in tokens if not i in stop_words]
    stemmer= PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return tokens


file_path = input("Enter the file path: ")
text = handle_input_file(file_path)
tokens = preprocess_text(text)
print(tokens)
# store the tokens in a file
file = open('tokens.txt', 'w')
file.write(str(tokens))
file.close()
