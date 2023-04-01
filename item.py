from tqdm import tqdm
from get_html import get_html
from setting import json_head,stop_word1,stop_word2,limit,proj_dir
import time
import re
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from certifycode import crack

# csv中的每个网址内容get并解析到website文件夹中

def item(startrow, city,leixing):
    data = pd.read_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv",header=None)
    data = data.iloc[:, 0].astype("str")
    endrow=data.shape[0]
    for i in tqdm(range(startrow, endrow)):
        item_url = data.iloc[i]
        # 定义搜索内容
        item_kw = f"{i}"
        # 发起请求
        response = get_html(url=item_url, kw=item_kw, head=json_head)

        if stop_word2 in response.text:
            time.sleep(limit)
            continue
        elif stop_word1 in response.text:
            startrow = i

            option = webdriver.ChromeOptions()
            option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            option.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=option) 
            driver.get(url=item_url)

            time.sleep(4)

            response = get_html(url=item_url, kw=item_kw, head=json_head)
            result = response.text
            if stop_word1 not in response.text:
                filename = re.findall(r"fangchan/(.*?).shtml?", item_url)[0] + ".html"
                with open(
                    f"{proj_dir}/{city}/{leixing}/website/{filename}", "w", encoding="utf-8"
                ) as tem:
                    tem.write(result)
                time.sleep(4)
            else:
                print(f'startrow={i}')
                break
        else:
            result = response.text
            filename = re.findall(r"fangchan/(.*?).shtml?", item_url)[0] + ".html"
            # 存储文件
            with open(
                f"{proj_dir}/{city}/{leixing}/website/{filename}", "w", encoding="utf-8"
            ) as tem:
                tem.write(result)
            time.sleep(4)