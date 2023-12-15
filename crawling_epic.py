from selenium import webdriver
from selenium.webdriver.common.by import By

def prev_article():
    href = [i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR,'dd > a[onclick^="javascript:fn_beforeAfter"]')][-1]
    driver.get(href)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://eiec.kdi.re.kr/policy/materialList.do")

    # get the first article
    driver.find_element(By.CSS_SELECTOR,
        '#ui_contents > div.page_conts-bar.policy_material > div#listArea > ul > li:nth-child(1) > a').click()\
    #j = 1 # 파일 번호 카운터
    while True:
        try:
            pdf_link = \
                [i.get_attribute("href") for i in driver.find_elements(By.CSS_SELECTOR,
                                                                       'div.view_top.downbtn_org > div.bot > div.downbtn_line > div.download_wrap > div.file_bubble > ul.con > li > a') if ".pdf" in i.text][0]
            driver.get(pdf_link)

            if driver.page_source == '<html><head></head><body></body></html>':
                driver.back()
            else:
                pass
        except IndexError:
            pass
        #prev_article()