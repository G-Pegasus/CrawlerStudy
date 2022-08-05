import csv
import requests
from bs4 import BeautifulSoup

url = "https://aa4bh.com/zipaitoupai/index.html"
resp = requests.get(url)
resp.encoding = 'utf-8'

f = open("av.csv", mode='w', encoding='utf-8')
csvwriter = csv.writer(f)

soup = BeautifulSoup(resp.text, "html.parser")
div = soup.find("div", class_="row col5 clearfix")
av_list = div.find_all("a", target="_blank")

av_info = []

for it in av_list:
    av_dict = {'url': "https://aa4bh.com" + it['href'], 'title': it['title']}
    av_info.append(av_dict.get("url"))
    av_info.append(av_dict.get("title"))
    csvwriter.writerow(av_info)
    av_info.clear()

f.close()
print('over!')


