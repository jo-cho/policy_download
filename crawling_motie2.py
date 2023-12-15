from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import requests
import os

def prev_article():
    href = driver.find_element(By.CSS_SELECTOR, 'a[title="이전 게시물로 이동"]').get_attribute('href')
    if not href:
        return
    driver.get(href)

def get_pdf_links(driver):
    pdf_links = []
    for a in driver.find_elements(By.CSS_SELECTOR, 'a[href*=".pdf"]'):
        pdf_links.append(a.get_attribute('href'))
    return pdf_links

def download_pdf(driver, pdf_link):
    try:
        response = requests.get(pdf_link)
        if response.status_code == 200:
            with open(os.path.basename(pdf_link), 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    chromedriver = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://www.motie.go.kr/motie/ne/presse/press2/bbs/bbsView.do?bbs_seq_n=157571&bbs_cd_n=81")

    # get the first article
    driver.find_element(By.CSS_SELECTOR,
                        '#content > article > div.common_list > table > tbody > tr:nth-child(1) > td.al > div > a').click()

    while True:
        pdf_links = get_pdf_links(driver)
        if not pdf_links:
            break
        for pdf_link in pdf_links:
            download_pdf(driver, pdf_link)
        driver.close()
        prev_article()