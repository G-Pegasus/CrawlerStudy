import csv

import requests
import re

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
page_content = resp.text
resp.close()

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)'
                 r'</span>.*?<span>(?P<num>.*?)</span>', re.S)

result = obj.finditer(page_content)

f = open("data.csv", mode="w")
csv_writer = csv.writer(f)

for it in result:
    # print(it.group("name") + "\t" + it.group("score") + "\t" + it.group("num") + "\t" + it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csv_writer.writerow(dic.values())
f.close()
print("over!")
