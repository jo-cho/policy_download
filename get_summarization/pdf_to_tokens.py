from pdfminer.high_level import extract_text
import sys
import nltk
from nltk.tokenize import word_tokenize
import os


pdf_path = "C:/Users/master/Downloads/epic_today/"

# nltk의 토큰화 기능을 사용하기 위한 자연어 처리 데이터 다운로드
nltk.download('punkt')


def tokenize_and_trim(text, max_tokens=4000):
    tokens = word_tokenize(text)
    return tokens[:max_tokens]

if __name__ == '__main__':
    pdf_list = os.listdir(pdf_path)
    for i in pdf_list:
        if i.endswith('.pdf'):
            text = extract_text(pdf_path+i)
            result = tokenize_and_trim(text)
            name = i.split('.')[0]
            sys.stdout = open(f'C:/Users/master/Downloads/epic_today/text_tokenized/{name}_tokens.txt', 'w', encoding='utf-8')
            print(result)
