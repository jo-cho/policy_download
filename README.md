**경제 정책 데이터 크롤링**

**Economic Policy Data Web Crawling**

---------------

### 데이터 크롤링(ver1)
- KDI EIEC 경제정책자료 수집 (ID, 제목, 발간처, 날짜, 내용 요약) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata.py)
- KDI EIEC 국내외연구자료 수집 (ID, 제목, 발간처, 날짜, 내용 요약) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata_research.py)

### 데이터 크롤링 및 원자료 PDF 다운로드 (ver2)
- KDI EIEC 경제정책자료 수집 (ID, 제목, 발간처, 날짜, 페이지수, 파일명1,2,3,4,5, 다운로드링크1,2,3,4,5) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_metadata.py)
  - 원문자료 PDF, HWP 파일 다운로드 가능
- KDI EIEC 국내외연구자료 수집 (ID, 제목, 발간처, 날짜, 페이지수, 파일명1,2,3,4,5, 다운로드링크1,2,3,4,5) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_research.py)

### 미국 재무부 보도자료 크롤링
- 

### 자동 요약 (in progress)
- PDF 텍스트 추출
- PDF 텍스트 토큰화(tokenize)
- 요약 후 엑셀 다운로드
- *요약 모델(ex. gpt4) 미탑재*


-------------

### Data Crawling (ver1)
- KDI EIEC Collection of economic policy documents (ID, title, publisher, date, content summary) [(link to code)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata.py)
- KDI EIEC Collection of domestic and international research papers (ID, title, publisher, date, content summary) [(link to code)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata_research.py)

### Data Crawling and Raw PDF Download (ver2)
- KDI EIEC Collection of economic policy documents (ID, title, publisher, date, number of pages, file names 1–5, download links 1–5) [(link to code)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_metadata.py)
  - Raw document PDF and HWP files available for download
- KDI EIEC Collection of domestic and international research papers (ID, title, publisher, date, number of pages, file names 1–5, download links 1–5) [(link to code)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_research.py)

### Automatic Summarization (in progress)
- PDF text extraction
- PDF text tokenization
- Summarization and Excel file download
- *Summarization models (e.g., GPT-4 API) not yet integrated*

