from selenium.webdriver.common.by import By
import time
from tqdm import tqdm
import pandas as pd
from selenium import webdriver
download_dir = "/Users/downloads/files_epic"

if __name__ == '__main__':
    # Chrome WebDriver 시작
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir
    })
    driver = webdriver.Chrome(options=options)

    # 웹페이지로 이동
    driver.get(
        "https://eiec.kdi.re.kr/policy/materialList.do?depth1=J0000&depth2=J0900&code=J0601&code=J0602&code=J0603&code=J0801&code=J0802&code=J0901&search_txt=&topic=&pg=1&pp=4400&type=J&device=pc")
    time.sleep(5)
    df_list = []
    start_num = 1
    end_num = 3621 # ~ 3621까지
    start_num2 = 3621
    end_num2 = 4346

    for n in tqdm(range(start_num, end_num+1)):
        # 제목, 부처 날짜 페이지 찾기
        title = driver.find_element(By.CSS_SELECTOR, f'#listArea > ul > li:nth-child({n}) > a > div > p').text # 자료 제목
        dept = driver.find_element(By.CSS_SELECTOR, f'#listArea > ul > li:nth-child({n}) > a > div > span:nth-child(2)').text
        date_page = driver.find_element(By.CSS_SELECTOR, f'#listArea > ul > li:nth-child({n}) > a > div > span:nth-child(3)').text # 날짜
        date, page = date_page.split()
        url = driver.find_element(By.CSS_SELECTOR, f'#listArea > ul > li:nth-child({n}) > a').get_attribute('href')  # url
        url = url.split('&pg')[0]
        num = url.split('num=')[1]

        # 파일 개수와 파일 제목 찾기

        file_names = []
        file_dn_links = []

        for i in range(1, 6):  # 최대 5개 항목에 대해 반복
            try:
                # 해당 항목이 존재하는 경우
                element = driver.find_element(By.CSS_SELECTOR,
                                                f'#listArea > ul > li:nth-child({n}) > div.download_wrap > div.file_bubble > ul > li:nth-child({i}) > a')
                file_name = element.get_attribute('textContent')
                file_dn_link = element.get_attribute('href').split('&dtime')[0]
            except:
                # 항목이 없는 경우 None으로 처리
                file_name = None
                file_dn_link = None
            file_names.append(file_name)
            file_dn_links.append(file_dn_link)

        df0 = pd.DataFrame({"자료명": title, "발간일": date, "발간처": dept, "페이지수": page, "URL": url,
                            "파일명1":file_names[0],"파일명2":file_names[1],"파일명3":file_names[2],"파일명4":file_names[3],"파일명5":file_names[4],
                            "다운로드링크1":file_dn_links[0],"다운로드링크2":file_dn_links[1],"다운로드링크3":file_dn_links[2],"다운로드링크4":file_dn_links[3],
                            "다운로드링크5":file_dn_links[4]}, index=[num])
        df_list.append(df0)

        # 파일 다운로드
        ul_element = driver.find_element(By.CSS_SELECTOR, f'#listArea > ul > li:nth-child({n}) > div.download_wrap > div.file_bubble > ul')
        li_elements = ul_element.find_elements('tag name', 'li')
        file_len = len(li_elements) # 파일개수

        # for i in range(1, file_len + 1):
        #     driver.get(f"https://eiec.kdi.re.kr/policy/callDownload.do?num={num}&filenum={i}")

    df = pd.concat(df_list, axis=0)
    print(df)
    df.to_excel("C:/Users/master/downloads/metadata.xlsx", engine='xlsxwriter')
