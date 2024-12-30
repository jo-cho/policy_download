from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import os, shutil

num_start = 76227 #오늘꺼 시작
num_end = 76260 #오늘꺼 마지막

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.getElementById('downloadsList').items;
        if (items.every(e => e.state === "COMPLETE"))
            return items.map(e => e.fileUrl || e.file_url);
        """)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    for n in range(num_start, num_end+1):
        driver.implicitly_wait(10)
        try:
            link = f"https://epts.kdi.re.kr/share?cte_seq={n}"
            driver.get(link)
            driver.implicitly_wait(5)
            #filepath = "C:/Users/master/Downloads/"
           # filename = max([filepath + f for f in os.listdir(filepath)], key=os.path.getctime)
           # if filename.endswith('.pdf'):
         #       shutil.move(src=os.path.join(filepath, filename), dst=filepath+f'{n}.pdf')
        except UnexpectedAlertPresentException:
            pass
    #paths = WebDriverWait(driver, 150, 1).until(every_downloads_chrome)
    #print(paths)