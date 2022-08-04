import requests

url = "https://movie.douban.com/j/chart/top_list"

params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

resp = requests.get(url=url, params=params, headers=headers)
# print(resp.json())

with open("movie.json", mode="w", encoding='utf-8') as f:
    f.write(resp.text)
print('over!')
resp.close()
f.close()
