from selenium import webdriver
from selenium.webdriver.common.by import By

def prev_article():
    href = [i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR,'dd > a[onclick^="javascript:fn_beforeAfter"]')][-1]
    driver.get(href)


if __name__ == '__main__':
    #chromedriver = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardList.do?bbsId=BBSMSTR_000000000008")

    # get the first article
    driver.find_element(By.CSS_SELECTOR,
        '#print_area > div.table_wrap.type_01 > form > table > tbody > tr:nth-child(1) > td.l > div > a').click()\
    #j = 1 # 파일 번호 카운터
    while True:
        try:
            hwp_link = \
                [i.get_attribute("href") for i in driver.find_elements(By.CSS_SELECTOR,'div.fileList > ul > li > a') if ".pdf" in i.text][0]
            #filename = f'R23{j}.pdf'
            driver.get(hwp_link)
            if driver.page_source == '<html><head></head><body></body></html>':
                driver.back()
            else:
                pass
        except IndexError:
            pass
        prev_article()