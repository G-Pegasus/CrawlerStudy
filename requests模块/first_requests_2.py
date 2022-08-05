import csv

import requests
import jsonpath
import json

url = "http://xinfadi.com.cn/getPriceData.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url=url, headers=headers)
html_str = resp.text
jsonobj = json.loads(html_str)

vege_name = jsonpath.jsonpath(jsonobj, '$..prodName')
vege_low = jsonpath.jsonpath(jsonobj, '$..lowPrice')
vege_avg = jsonpath.jsonpath(jsonobj, '$..avgPrice')
vege_high = jsonpath.jsonpath(jsonobj, '$..highPrice')
vege_date = jsonpath.jsonpath(jsonobj, '$..pubDate')
count = len(vege_name)
vege = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(count):
    for j in vege_name:
        vege[i].append(j)
        vege_name.remove(j)
        break
    for j in vege_low:
        vege[i].append(j)
        vege_low.remove(j)
        break
    for j in vege_avg:
        vege[i].append(j)
        vege_avg.remove(j)
        break
    for j in vege_high:
        vege[i].append(j)
        vege_high.remove(j)
        break
    for j in vege_date:
        vege[i].append(j)
        vege_date.remove(j)
        break

# with open("vegetable.json", mode="w", encoding='utf-8') as f:
#     f.write(resp.text)
# print('over!')

with open("vegetable.csv", mode="w", encoding='utf-8') as f2:
    for i in vege:
        csv.writer(f2).writerow(i)
print('over!')
resp.close()
# f.close()
f2.close()
