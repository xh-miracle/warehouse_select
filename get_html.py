# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:15:02 2023

@author: wangyanghao
"""

import requests
from bs4 import BeautifulSoup as bf
def get_html(url, kw, head):
    param = {"wd": kw} # 关键词
    response = requests.get(url=url, params=param, headers=head)
    return response
def get_result(response):
    result = response.text
    obj = bf(result, "html.parser") # bs4解码,参数2也可以用lxml 或者 html5lib
    return obj