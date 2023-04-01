from get_html import get_html
from get_html import get_result
from setting import json_head,proj_dir
from page import get_index
from page import page
from allcsv import allcsv
from item import item
from pathlib import Path
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from certifycode import crack
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# cities = ['hrb','dq','qqhr','mdj','suihua','jms','jixi','sys','hegang','heihe','yich','qth','dxal','shanda','shzhaodong','zhaozhou']
# cities = ['chuzhou']
citylist=pd.read_excel(f'{proj_dir}/citylist.xlsx')
pro="广东"
pro_city = citylist.loc[citylist['pro']==pro,'index']

for city in pro_city:
#leixing = 厂房、仓库、土地
    for leixing in ["tudi","changfang","cangkucf"]: 
        pn_url=f"https://{city}.58.com/{leixing}/" # 网址
        print(f'开始{city}的{leixing}')
        if __name__ == "__main__":
            '''pathlib.Path.mkdir
            mkdir(parents=True, exist_ok=True)
            parents：如果父目录不存在，是否创建父目录。
            exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
            '''
            Path(f"{proj_dir}/{city}/{leixing}/website").mkdir(parents=True, exist_ok=True)# 创建文件夹
            index=get_index(city,leixing,pn_url) # 获取最大页码-找网页规律
            print(f'页数={index}')

            if index!=0:
                startpage=1
                endpage=index # 最大页码
                page(startpage,endpage,pn_url=pn_url,city=city,leixing=leixing) # 获取每一页的网址，有异常则打印页码
                # page(startpage=4,endpage=8,pn_url=pn_url,city=city,leixing=leixing)    
            html_cnt = allcsv(city,leixing) # 每个文件夹下的html中的网址写入csv,返回pn_html个数

            startrow=0
            if html_cnt>0:
                item(startrow, city=city,leixing=leixing) # csv中的每个网址内容get并解析到website文件夹中
   
# option = webdriver.ChromeOptions()
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(chrome_options=option) 
# driver.get(url="https://callback.58.com/antibot/verifycode?serialId=96cc66e1003da53756b83b6ac7ab0ba4_8bd26c30a6cd4e6e871d0fe0045ba7d8&code=22&sign=d534c692ad90b5a956027b3b4f77f8d0&namespace=fangchan_business_pc&url=https%253A%252F%252Fbozhou.58.com%252Ffangchan%252F53108012701715x.shtml%253F")
# btn = driver.find_element(By.XPATH,r'//div[@class="code_num"]')
# ActionChains(driver).move_to_element(btn).perform()
# ActionChains(driver).click().perform()
# btn.click()
# driver.quit()

#item(startrow=77, city=city,leixing=leixing)
    


