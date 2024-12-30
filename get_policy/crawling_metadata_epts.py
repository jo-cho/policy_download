from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


if __name__ == '__main__':
    driver = webdriver.Chrome()
    count=0
    df_list = []
    for n in range(200):
        link = "https://epts.kdi.re.kr/polcTmsesSrvc/gvdpt?SEARCH_CTE_SEQ=22796&BIG_CD=GVDPT00046&MID_CD=GVDPT00085&SML_CD=GVDPT00086"
        try:
            driver.get(link)
        except Exception:
            print(f"{link} - 주소 없음")
            continue