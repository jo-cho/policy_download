from selenium import webdriver

num_start = 246126 #오늘꺼 시작
num_end = 246188 #오늘꺼 마지막


if __name__ == '__main__':
    driver = webdriver.Chrome()
    for n in range(num_start, num_end+1):
        try:
            pdf_link = f"https://eiec.kdi.re.kr/policy/callDownload.do?num={n}&filenum=1"
            driver.get(pdf_link)
            if driver.page_source == '<html><head></head><body></body></html>':
                driver.back()
            else:
                pass
        except IndexError:
            pass