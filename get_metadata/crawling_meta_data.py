from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

num_start = 245419	 # 시작
num_end = 246695 # 마지막

if __name__ == '__main__':
    driver = webdriver.Chrome()

    df_list = []
    for n in range(num_start, num_end + 1):
        link = f"https://eiec.kdi.re.kr/policy/materialView.do?num={n}"
        try:
            driver.get(link)
            # 제목 찾기
            title = driver.find_element(By.CSS_SELECTOR,
                f'#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org > strong').text
            # 날짜 찾기
            date = driver.find_element(By.CSS_SELECTOR,
                f'#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org > div > div.downbtn_line > span:nth-child(1)').text
            # 부처 찾기
            deprt = driver.find_element(By.CSS_SELECTOR,
                f'#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org > div > span').text
            # 초록 찾기
            summ = driver.find_element(By.CSS_SELECTOR,
                f'#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_body > div').text

            df0 = pd.DataFrame({"제목":title,"날짜":date,"발간처":deprt,"요약":summ}, index=[n])
            df_list.append(df0)

        except Exception:
            print(f"{link} - 주소 없음")
            continue

    df = pd.concat(df_list, axis=0)

    print(df)
    df.to_excel(f"C:/Users/master/Downloads/epic_metadata_2312.xlsx")