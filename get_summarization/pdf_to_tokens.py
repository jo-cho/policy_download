from pdfminer.high_level import extract_text
import sys
import nltk
from nltk.tokenize import word_tokenize
import os
import re  # 정규 표현식 모듈 추가

pdf_path = "pdf/"

# nltk의 토큰화 기능을 사용하기 위한 자연어 처리 데이터 다운로드
nltk.download('punkt')

def remove_symbols(text):
    # 정규 표현식을 사용하여 특수 문자 제거
    return re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]', '', text)

def tokenize_and_trim(text, max_tokens=4000):
    # 텍스트에서 기호 제거
    text = remove_symbols(text)
    tokens = word_tokenize(text)
    return tokens[:max_tokens]

if __name__ == '__main__':
    pdf_list = os.listdir(pdf_path)
    for i in pdf_list:
        if i.endswith('.pdf'):
            text = extract_text(pdf_path+i)
            result = tokenize_and_trim(text)
            name = i.split('.')[0]
            with open(f'C:/Users/master/Documents/GitHub/policy_download/get_summarization/text_tokenized/{name}_tokens.txt', 'w', encoding='utf-8') as f:
                print(result, file=f)
