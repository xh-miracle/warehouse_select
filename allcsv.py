from setting import proj_dir
import glob
from bs4 import BeautifulSoup as bf
import pandas as pd
# 每个文件夹下的html中的网址写入csv

# def allcsv(city,leixing):
#     html_list = glob.glob(f"{proj_dir}/{city}/{leixing}/*.html")  # 查看同文件夹下的html文件列表
#     f = open(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", mode="a")
#     for result in html_list:  # 循环读取同文件夹下的html文件
#         obj = bf(open(result, encoding="utf-8"), features="html.parser")  # features值可为lxml
#         for item in obj.select('ul[class="list-main-style"] a'):
#             detail_url = item.get("href")
#             f.write("%s\n" % (detail_url))
#     f.close()
#     data = pd.read_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", header=None)
#     data = data.iloc[:, 0].astype("str").str.split("prd", expand=True)[0] # expand让分割内容变成2列
#     data = data.drop_duplicates() # 去重
#     data.to_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv",mode='w',header=None,index=False)
#     return 
# 'http' not in '//qqhr.58.com/fangchan/34086202572731x.shtml?'


# def allcsv(city,leixing):
#     html_list = glob.glob(f"{proj_dir}/{city}/{leixing}/*.html")  # 查看同文件夹下的html文件列表
#     f = open(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", mode="a")
#     for result in html_list:  # 循环读取同文件夹下的html文件
#         obj = bf(open(result, encoding="utf-8"), features="html.parser")  # features值可为lxml
#         for item in obj.select('ul[class="list-main-style"] a'):
#             detail_url = item.get("href")
#             if 'https:' not in str(detail_url):
#                 detail_url = f"https:{detail_url}"
#                 f.write("%s\n" % (detail_url))
#             else:
#                 f.write("%s\n" % (detail_url))
#     f.close()
#     data = pd.read_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", header=None)
#     data = data.iloc[:, 0].astype("str").str.split("prd", expand=True)[0] # expand让分割内容变成2列
#     data = data.drop_duplicates() # 去重
#     data.to_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv",mode='w',header=None,index=False)
#     return 
def allcsv(city,leixing):
    html_list = glob.glob(f"{proj_dir}/{city}/{leixing}/*.html")  # 查看同文件夹下的html文件列表
    html_cnt=len(html_list)
    if html_cnt>0:
        f = open(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", mode="a")
        for result in html_list:  # 循环读取同文件夹下的html文件
            obj = bf(open(result, encoding="utf-8"), features="html.parser")  # features值可为lxml
            for item in obj.select('ul[class="list-main-style"] a'):
                detail_url = item.get("href")
                if 'https:' not in str(detail_url):
                    detail_url = f"https:{detail_url}"
                    f.write("%s\n" % (detail_url))
                else:
                    f.write("%s\n" % (detail_url))
        f.close()
        data = pd.read_csv(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", header=None)
        data = data.iloc[:, 0].astype("str").str.split("prd", expand=True)[0] # expand让分割内容变成2列
        data = data.drop_duplicates() # 去重
    # else: # 注释掉else，没有pg_html就不输出csv，提高效率
    #     f = open(f"{proj_dir}/{city}/{leixing}/{leixing}.csv", mode="a")
    #     f.write(f'{city}{leixing}搜索暂无结果')
    #     f.close()
    #     print(f'{city}{leixing}搜索暂无结果')
    return html_cnt