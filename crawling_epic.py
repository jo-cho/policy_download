from selenium import webdriver
from selenium.webdriver.common.by import By

#def prev_article():
#    href = [i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR,'dd > a[onclick^="javascript:fn_beforeAfter"]')][-1]
 #   driver.get(href)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://eiec.kdi.re.kr/policy/materialList.do")
    for n in range(1,21):
        # get the first article
        driver.find_element(By.CSS_SELECTOR,
            f'#ui_contents > div.page_conts-bar.policy_material > div#listArea > ul > li:nth-child({n}) > a').click()\

        driver.find_element(By.CSS_SELECTOR,
            'div.view_top.downbtn_org > div.bot > div.downbtn_line > div.download_wrap').click()\

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

        driver.find_element(By.CSS_SELECTOR,
                            'div.view_botm > a').click()