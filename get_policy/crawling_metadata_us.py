from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

num_start = 2001 # 
num_end = 2800 # 

nums = num_end-num_start+1

who = 'jy' #yymm

# 'sb' (Scott Bessent)
# 'jy' (Janet Yellen)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    count=0
    df_list = []
    for n in range(num_start, num_end + 1):
        link = f"https://home.treasury.gov/news/press-releases/{who}{n:04}"
        try:
            driver.get(link)
            # title
            title = driver.find_element(By.CSS_SELECTOR,
                '#block-hamilton-page-title > h2 > span').text
            # date
            date = driver.find_element(By.CSS_SELECTOR,
                '#block-hamilton-content > article > div > div.date-format.field.field--name-field-news-publication-date.field--type-datetime.field--label-hidden.field__item > time').text
            # cat
            category = driver.find_element(By.CSS_SELECTOR,
                '#block-views-block-news-category-block > div > div > div > div > div').text
            # content
            content = driver.find_element(By.CSS_SELECTOR,
                '#block-hamilton-content > article > div > div.clearfix.text-formatted.field.field--name-field-news-body.field--type-text-long.field--label-hidden.field__item').text
            # df
            df0 = pd.DataFrame({"title":title,"date":date,"category":category,"content":content}, index=[f'{who}{n:04}'])
            df_list.append(df0)
            count += 1
            if count % 10 == 0:
                print(f"now {count}/{nums} completed -- {round(100*count/nums,2)}%")
        except Exception:
            print(f"{link} - no address")
            continue

    df = pd.concat(df_list, axis=0)
    print(f"Total {len(df)} docs crawling completed")
    # print(df)

    # download in excel
    df.to_excel(f"data/ustreasurynews_metadata_{who}5.xlsx", engine='xlsxwriter')