#from tudiparse import parse_tudi
from fangchanparse import parse_fc
from setting import proj_dir
import pandas as pd
from tqdm import tqdm

citylist=pd.read_excel(f'{proj_dir}/citylist.xlsx')
pro="黑龙江"
df=pd.read_excel(f'{proj_dir}/租金.xlsx')
pro_city = citylist.loc[citylist['pro']==pro,'index']
for city in tqdm(pro_city):
    for leixing in ['tudi','changfang','cangkucf']:
        parse_fc(city,leixing,df)
df.to_excel(f'{proj_dir}/{pro}租金.xlsx',index=False)


