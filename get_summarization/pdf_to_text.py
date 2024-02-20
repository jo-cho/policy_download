from pdfminer.high_level import extract_text
import os
import re  # 정규 표현식 모듈 추가

pdf_path = "pdf/"
output_path = "C:/Users/master/Documents/GitHub/policy_download/get_summarization/text_extracted/"

if __name__ == '__main__':
    # 지정한 디렉토리에서 PDF 파일 목록을 가져옴
    pdf_list = os.listdir(pdf_path)
    for pdf_file in pdf_list:
        if pdf_file.endswith('.pdf'):
            # PDF 파일에서 텍스트 추출
            text = extract_text(pdf_path + pdf_file)
            # 결과 텍스트를 txt 파일로 저장
            output_filename = os.path.splitext(pdf_file)[0] + "_extracted.txt"
            with open(output_path + output_filename, 'w', encoding='utf-8') as f:
                f.write(text)
            print(len(text))