import pandas as pd
import os
from datetime import datetime

text_folder_path = "C:/Users/master/Downloads/epic_today/text_tokenized/"
text_file_list = os.listdir(text_folder_path)

# Chat API 예제

############

text_data = []
summary_data = []
num_data = []
for file_name in text_file_list:
    if file_name.endswith('.txt'):
        file_path = os.path.join(text_folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            text_data.append(file_contents)
            summarized_contents = summarize(file_contents)
            summary_data.append(summarized_contents)
            num_name = file_name.split('_')[0]
            num_data.append(num_name)

name = datetime.today().strftime("%Y%m%d")
df = pd.DataFrame({"num":num_data, "summary":summary_data, "input_text":text_data})
df.to_excel(f"C:/Users/master/Downloads/epic_today/{name}.xlsx")