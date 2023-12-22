from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait

num_start = 246167 #오늘꺼 시작
num_end = 246187 #오늘꺼 마지막

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
            link = f"https://eiec.kdi.re.kr/policy/callDownload.do?num={n}&filenum=1"
            driver.get(link)
            driver.implicitly_wait(5)
        except UnexpectedAlertPresentException:
            pass
    paths = WebDriverWait(driver, 150, 1).until(every_downloads_chrome)
    print(paths)