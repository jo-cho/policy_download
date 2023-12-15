from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

def prev_article():
    href = driver.find_element(By.CSS_SELECTOR,'a[title="이전 게시물로 이동"]').get_attribute('href')
    driver.get(href)


if __name__ == '__main__':
    chromedriver = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://www.motie.go.kr/motie/ne/presse/press2/bbs/bbsView.do?bbs_seq_n=157571&bbs_cd_n=81")

    # get the first article
    # driver.find_elements(By.CSS_SELECTOR,
    #     '#content > article > div.common_list > table > tbody > tr:nth-child(1) > td.al > div > a').click()
    while True:
        try:
            hwp_link = \
                [i.get_attribute("href") for i in driver.find_elements(By.CSS_SELECTOR,'a[title="파일을 다운로드 받습니다."]') if i.text.endswith(".hwp")][0]
            driver.get(hwp_link)
            if driver.page_source == '<html><head></head><body></body></html>':
                driver.back()
            else:
                pass
        except IndexError:
            pass
        prev_article()
