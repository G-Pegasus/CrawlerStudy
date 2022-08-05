import requests
from bs4 import BeautifulSoup

url = "https://umei.cc/bizhitupian/weimeibizhi"
resp = requests.get(url)
resp.encoding = 'utf-8'

main_soup = BeautifulSoup(resp.text, "html.parser")
div = main_soup.find("div", class_="swiper-box").find_all("a")

for a in div:
    href = "https://umei.cc" + a['href']
    child_resp = requests.get(href)
    child_resp.encoding = 'utf-8'
    child_text = child_resp.text

    # 找到图片的url
    child_soup = BeautifulSoup(child_text, "html.parser")
    section = child_soup.find("section", class_="img-content")
    img = child_soup.find('img')
    src = img.get('src')

    img_resp = requests.get(src)
    img_name = src.split('/')[-1]

    # 下载图片到指定文件夹
    with open('img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)

    print('over!', img_name)

print('all over!')



