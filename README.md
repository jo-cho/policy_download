**KDI 경제정보센터 데이터 크롤링**

---------------

### 데이터 크롤링(ver1)
- 경제정책자료 수집 (ID, 제목, 발간처, 날짜, 내용 요약) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata.py)
- 국내외연구자료 수집 (ID, 제목, 발간처, 날짜, 내용 요약) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_metadata_research.py)

### 데이터 크롤링 및 원자료 PDF 다운로드 (ver2)
- 경제정책자료 수집 (ID, 제목, 발간처, 날짜, 페이지수, 파일명1,2,3,4,5, 다운로드링크1,2,3,4,5) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_metadata.py)
  - 원문자료 PDF, HWP 파일 다운로드 가능
- 국내외연구자료 수집 (ID, 제목, 발간처, 날짜, 페이지수, 파일명1,2,3,4,5, 다운로드링크1,2,3,4,5) [(파일 바로가기)](https://github.com/jo-cho/policy_download/blob/main/get_policy/crawling_pdf_metadata2.py)



### 자동 요약 (in progress)
- PDF 텍스트 추출
- PDF 텍스트 토큰화(tokenize)
- 요약 후 엑셀 다운로드
- *요약 모델(ex. gpt4) 미탑재*
