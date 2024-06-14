from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

num_start = 132565 # 시작
num_end = 152993 # 마지막

nums = num_end-num_start+1

month = '1601_2006' #yymm

if __name__ == '__main__':
    driver = webdriver.Chrome()
    count=0

    df_list = []
    for n in range(num_start, num_end + 1):
        link = f"https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000{n}" # 국외 자료도 국내 주소(domesticView)에 있긴 있음!
        try:
            driver.get(link)
            # 제목 찾기
            title = driver.find_element(By.CSS_SELECTOR,
                '#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org.css_pdright > strong').text
            # 날짜 찾기
            date = driver.find_element(By.CSS_SELECTOR,
                '#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org.css_pdright > div > div.downbtn_line > span').text
            # 부처 찾기
            deprt = driver.find_element(By.CSS_SELECTOR,
                '#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_top.downbtn_org.css_pdright > div > span').text
            # 초록 찾기
            summ = driver.find_element(By.CSS_SELECTOR,
                '#ui_contents > div.page_conts-bar.economy_multi > div.view_comm_style > div.view_body > div').text

            df0 = pd.DataFrame({"자료명":title,"발간일":date,"발간처":deprt,"요약":summ}, index=[n])
            df_list.append(df0)
            count += 1
            if count % 10 == 0:
                print(f"현재 {count}개/{nums}개 자료 크롤링 완료 -- {round(100*count/nums,2)}%")
        except Exception:
            print(f"{link} - 주소 없음")
            continue

    df = pd.concat(df_list, axis=0)
    print(f"총 {len(df)}개 자료 크롤링 완료")
    # print(df)
    df.to_excel(f"data/research_metadata_{month}.xlsx", engine='xlsxwriter')