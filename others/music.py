import requests
from Crypto.Cipher import AES
import base64
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token=09c66ec1a175f302f5850f6da5f842c0"

data = {
    "csrf_token": "09c66ec1a175f302f5850f6da5f842c0",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_29816800",
    "threadId": "R_SO_4_29816800"
}

e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "C0DocUOxS6L0zO3b"


def get_encSecKey():
    return "ab72e6e2389d7bf002ccde8d48b2542f2c1fbf8e4559600cae40cb02b248aff92f18eb8da805dba9f102b4e3fefaa219b7f48fff9c4948365aa4fe97accf78d3368513229d62d926763807cf3aecf68e11a3d3e2497895d55eef1b5ba6522ed8893ee310c301f69b611660003f976a5b2c80d360e2034b353b8ff4cd68f9f241"


def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second


# AES 加密需加密16位的明文，不够就补到16位
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


# 用AES将参数加密，得到需要的 params
def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    # IV 就是偏移量，16位，采用 CBC 模式
    aes = AES.new(key=key.encode('utf-8'), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode('utf-8'))
    return str(base64.b64encode(bs), 'utf-8')


resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

with open("comments.json", mode="w", encoding='utf-8') as f:
    f.write(resp.text)

f.close()

# 补充
""" 网页js代码加密过程
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""
