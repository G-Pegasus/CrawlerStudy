import requests
from lxml import etree
import csv

url = "https://www.zbj.com/search/service/?l=0&kw=%E5%AE%89%E5%8D%93&r=1"

resp = requests.get(url)
# 解析HTML文件
html = etree.HTML(resp.text)

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
info = []
for div in divs:
    newList = []
    title = div.xpath('./a/div[2]/div[1]/div/text()')[0]
    price = div.xpath('./div[3]/div[1]/span/text()')[0]
    content = div.xpath('./div[3]/a/text()')[0]
    newList.append(title)
    newList.append(price)
    newList.append(content)
    info.append(newList)

with open('zhubajie.csv', mode='w', encoding='utf-8') as f:
    for i in info:
        csv.writer(f).writerow(i)

f.close()
print('over!')

