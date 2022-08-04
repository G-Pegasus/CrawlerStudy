import requests
import re
import csv

# 域名
domain = "https://www.dytt89.com"

resp = requests.get(domain, verify=False)  # 去掉安全认证
resp.encoding = 'gb2312'

obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="('
                  r'?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group('ul')

    # 提取页面子链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        child_href = domain + itt.group('href')
        child_href_list.append(child_href)  # 将子页面链接保存起来

f = open("movie.csv", mode="w", encoding='utf-8')
csv_writer = csv.writer(f)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    # print(result3.group("movie").strip())
    # print(result3.group("download"))

    dic = result3.groupdict()
    dic["movie"] = dic["movie"].strip()
    csv_writer.writerow(dic.values())

f.close()
print('over!')
