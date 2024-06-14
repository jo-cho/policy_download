from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#num_start = 249781 # 시작 번호
#num_end = 250977 # 마지막 번호

#nums = num_end-num_start+1

#month = '2404' #yymm

if __name__ == '__main__':
    driver = webdriver.Chrome()
    count=0
    df_list = []
    for n in range(20):
        link = "https://epts.kdi.re.kr/polcTmsesSrvc/them?SEARCH_CTE_SEQ=77325&BIG_CD=RELT_THEM00002&MID_CD=RELT_THEM00034&SML_CD=RELT_THEM00044"
        try:
            driver.get(link)
        except Exception:
            print(f"{link} - 주소 없음")
            continue