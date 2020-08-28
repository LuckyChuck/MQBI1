# 使用request + BeautifulSoup提取12365auto投诉信息
import requests
from bs4 import BeautifulSoup
import pandas as pd

# # 请求URL
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'

# 根据request_url得到soup
def get_page_content(request_url):
    # 得到页面的内容,chrome版本为自己浏览器版本（刚更新）,但通过实验，不必与自己浏览器版本完全契合仍不影响结果，表示未知
    headers={'user-agent': 'Chrome/85.0.4183.83'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    #print(content)
    # 通过content创建BeautifulSoup对象,此处不用加 from_encoding='utf-8'，因为python3默认格式位utf8
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)
    return soup

# 分析当前页面的投诉
def analysis(soup):
    # 找到完整的投诉信息框
    temp = soup.find('div',class_="tslb_b")
    # 创建DataFrame，自定义列名
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            id,brand,car_model,type,desc,problem,datetime,status = td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            #print(id,brand,car_model,type,desc,problem,datetime,status)
            temp['id'],temp['brand'],temp['car_model'],temp['type'],temp['desc'],temp['problem'],temp['datetime'],temp['status'] =  id,brand,car_model,type,desc,problem,datetime,status
            df = df.append(temp,ignore_index=True)
    return df        

dfs = analysis(get_page_content(url))   
print(dfs)    


   






