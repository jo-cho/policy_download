from selenium import webdriver

num_start = 197568876
num_end = 197570597

if __name__ == '__main__':
    driver = webdriver.Chrome()
    for num in range(num_start, num_end+1):
        try:
            pdf_link = f'https://www.korea.kr/common/download.do?fileId={num}&tblKey=GMN'
            driver.get(pdf_link)
            if driver.page_source == '<html><head></head><body></body></html>':
                driver.back()
            else:
                pass
        except IndexError:
            pass