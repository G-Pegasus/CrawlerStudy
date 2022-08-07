import requests

# 第一种方式，通过session，登录账号，记得网页抓包勾选保存日志，这样才能显示login (Preserve log)
# 第二种方式，直接输入Cookie
url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
urlLogin = 'https://passport.17k.com/ck/user/login'
session = requests.session()

headers = {
    "Cookie": "GUID=a18c9cee-38e6-4f14-8fb0-b379e343f44b; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1659856730; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F19%252F99%252F64%252F97706499.jpg-88x88%253Fv%253D1659857593000%26id%3D97706499%26nickname%3D%25E6%258C%25BD%25E5%25BC%25A6%25E6%2585%2595%25E7%25AC%2599ya%26e%3D1675410029%26s%3D8a6d4f4a549227ed; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297706499%22%2C%22%24device_id%22%3A%22182772bb87e7eb-0c7aad4905c172-26021a51-1638720-182772bb87f1488%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22a18c9cee-38e6-4f14-8fb0-b379e343f44b%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1659858265"
}

data = {
    "loginName": "13394414991",
    "password": "liutongji8512"
}
session.post(urlLogin, data=data)
resp = requests.get(url, headers=headers)
resp1 = session.get(url)

for i in range(len(resp1.json()['data'])):
    print(resp1.json()['data'][i]['bookName'])
