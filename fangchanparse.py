import glob     
from setting import proj_dir
from bs4 import BeautifulSoup as bf
import re
import pandas as pd

def parse_fc(city,leixing,df):    
    html_list = glob.glob(f"{proj_dir}/{city}/{leixing}/website/*.html")  # 查看同文件夹下的html文件
    for result in html_list:  # 循环读取同文件夹下的html文件
        obj = bf(open(result, encoding="utf-8"), features="html.parser")  # features值可为lxml

        pattern = re.compile(r"var __baseInfo =(.*?);$", re.MULTILINE | re.DOTALL)# 将正则语言编译成一个pattern模式，具体功能：查找var __baseInfo之后的内容(.*?)任意字符-0次多次-不管有没有
        script = obj.find('script', text=pattern).text # 用编译的pattern查找'script'
        
        c=[' '.join([i.strip() for i in j.strip().split('\n')]) for j in [obj.find('div',class_="house-basic-poster-wrapper").text]][0]
        d=[x.strip() for x in c.split(' ') if x.strip()]
        if len(d)>2 and re.findall(r'营业执照编码：(.*)',d[2]):
            d[2]=re.findall(r'营业执照编码：(.*)',d[2])[0]
        else:
            for i in range(len(d),3):
                d.append("")
        
        if leixing=="changfang" or leixing=="cangkucf":
            list=[re.findall('infoId:\s"(\d+)"', script)[0],#infoId
            re.findall('houseId:\s"(\d+)"',script)[0],#houseId
            re.sub('\xa0','',obj.select('div[class="house-title"] h1')[0].text.strip()),#house-title
            obj.select('span[class="house_basic_title_money_num"]')[0].text,#house_basic_title_money_num
            obj.select('span[class="house_basic_title_money_unit"]')[0].text,#house_basic_title_money_unit
            obj.select('span[class="house_basic_title_money_num_second"]')[0].text.strip().split("\n")[0],#house_basic_title_money_num_second
            obj.select('p[class="house_basic_title_info"] span')[0].text,#建筑面积
            obj.select('p[class="house_basic_title_info"] span')[1].text,#厂房类型
            obj.select('p[class="house_basic_title_info"] span')[2].text,#起租面积
            "",#规划用途
            "",#支付方式
            "",#所有权
            obj.select('div[class="house_basic_title_info_2"] p')[0].text.split("\n")[2].strip(),#区域
            obj.select('div[class="house_basic_title_info_2"] p[class="p_2"] span[class="address"]')[0].text,#地址
            d[0],#poster-name
            d[1],#poster-company-4
            d[2],#zhizhao hoverSection
            re.findall('lng:\s(\d+\.\d+|\d+)',script)[0],#lng
            re.findall('lat:\s(\d+\.\d+|\d+)',script)[0],#lat
            "bd09",#crs
            obj.find(attrs={"http-equiv": "mobile-agent"})['content'].split("url=")[1], #URL
            obj.select('article[class="detail"]')[0].text, #描述
            leixing#类型
            ]
            df.loc[len(df.index)]=list
        else:
            list=[re.findall('infoId:\s"(\d+)"', script)[0],#infoId
            re.findall('houseId:\s"(\d+)"',script)[0],#houseId
            re.sub('\xa0','',obj.select('div[class="house-title"] h1')[0].text.strip()),#house-title
            obj.select('span[class="house_basic_title_money_num"]')[0].text,#house_basic_title_money_num
            obj.select('span[class="house_basic_title_money_unit"]')[0].text,#house_basic_title_money_unit
            obj.select('span[class="house_basic_title_money_num_second"]')[0].text.strip().split("\n")[0],#house_basic_title_money_num_second
            obj.select('p[class="house_basic_title_info"] span')[0].text,#建筑面积
            "",#厂房类型
            "",#起租面积
            obj.select('p[class="house_basic_title_info"] span')[1].text,#规划用途
            obj.select('p[class="house_basic_title_info"] span')[2].text,#支付方式
            obj.select('p[class="house_basic_title_info"] span')[4].text,#所有权
            obj.select('div[class="house_basic_title_info_2"] p')[0].text.split("\n")[2].strip(),#区域
            obj.select('div[class="house_basic_title_info_2"] p[class="p_2"] span[class="address"]')[0].text,#地址
            d[0],#poster-name
            d[1],#poster-company-4
            d[2],#zhizhao hoverSection
            re.findall('lng:\s(\d+\.\d+|\d+)',script)[0],#lng
            re.findall('lat:\s(\d+\.\d+|\d+)',script)[0],#lat
            "bd09",#crs
            obj.find(attrs={"http-equiv": "mobile-agent"})['content'].split("url=")[1], #URL
            obj.select('article[class="detail"]')[0].text, #描述
            leixing #类型
            ]
            df.loc[len(df.index)]=list