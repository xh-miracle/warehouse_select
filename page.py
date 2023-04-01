# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:15:27 2023

@author: wangyanghao
获取每一页的网址，生成html(pn1、pn2…)，有异常则打印页码
"""

from get_html import get_html,get_result
from setting import json_head
import time
from tqdm import tqdm
from setting import stop_word1,stop_word2,proj_dir,limit
# from certifycode import crack
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#from certifycode import crack

def get_index(city,leixing,pn_url):
    # 定义搜索内容
    kw = "pagelist" # 关键词
    reponse = get_html(pn_url, kw, json_head) # request.get返回网址响应(添加请求头和参数)
    obj = get_result(reponse) # bs4解析html
    if '搜索暂无结果，查看下其他内容吧' not in obj.text:
        if obj.find("div", class_="pager").find_all("a"):
            page = obj.find("div", class_="pager").find_all("a") # 定位页码标签
            if len(page)>3: # 网址>2页
                maxpage = page[2].get("href") # 例如https://qqhr.58.com/changfang/pn2/ 齐齐哈尔厂房第2页
                new_url = maxpage[: maxpage.index("?") + 1].split("pn")
                index = int(new_url[1].split("/")[0]) + 1 
            else:
                maxpage = page[-2].get("href") # 倒数第二个（最后1个是"下一页"）
                new_url = maxpage[: maxpage.index("?") + 1].split("pn")
                index = int(new_url[1].split("/")[0]) + 1 
        elif obj.find("div", class_="pager"): # 网页源码找不到class_="pager"(可能只有1页)
            index = 2 
        else: # ???好像没有这种场景
            index=0
    else: # qth没有土地：'搜索暂无结果，查看下其他内容吧'
        index=0
    return index

def page(startpage, endpage,pn_url,city,leixing):
    for i in tqdm(range(startpage, endpage)):
        # 定义url的地址
        page_url = f"{pn_url}pn{i}/?" # 例如https://qqhr.58.com/changfang/pn2/ 齐齐哈尔厂房第2页
        # 定义搜索内容
        page_kw = f"pn{i}"
        response = get_html(url=page_url, kw=page_kw, head=json_head)

        if stop_word2 in response.text:
            time.sleep(limit) # 如果"没有找到相关信息"——休眠12秒，继续下一页
            continue
        elif stop_word1 in response.text: # 如果"访问过于频繁，本次访问做以下验证码校验。"——就弹出窗口手动验证
            startpage = i
            option = webdriver.ChromeOptions()
            option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
            option.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=option) 
            driver.get(url=pn_url)

            time.sleep(4)

            response = get_html(url=page_url, kw=page_kw, head=json_head)
            result = response.text
            if stop_word1 not in response.text:
                filename = page_kw + ".html"
                with open(
                    f"{proj_dir}/{city}/{leixing}/{filename}", "a", encoding="utf-8"
                ) as tem:
                    tem.write(result)
                time.sleep(limit)
            else:
                print(f'startpage={i}') # 还是报错"访问过于频繁，本次访问做以下验证码校验。"——打印页码
                break # 跳出，继续下一页

        else: # 没有异常词语——输出结果
            result = response.text
            filename = page_kw + ".html"
            # 存储文件
            with open(
                f"{proj_dir}/{city}/{leixing}/{filename}", "a", encoding="utf-8"
            ) as tem:
                tem.write(result)
            time.sleep(limit)