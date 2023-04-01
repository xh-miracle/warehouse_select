from pathlib import Path
import json

stop_word1 = "访问过于频繁，本次访问做以下验证码校验。"
stop_word2 = "没有找到相关信息"
brower_header = open('D:/导师/测试爬虫/brower_header.json',mode='r') # 读取json文件-请求头
json_head = json.load(brower_header)
#resolve()返回绝对路径，parent返回上一级目录
proj_dir = Path(__file__).resolve().parent
limit=3




