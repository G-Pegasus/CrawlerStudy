import re

# findall: 匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "中国移动：10086，中国电信：10000")
print(lst)
print("-----")
# finditer: 匹配字符串中所有的内容，返回一个迭代器，效率更高
it = re.finditer(r"\d+", "中国移动：10086，中国电信：10000")
for i in it:
    print(i.group())
print("-----")
# search: 找到一个结果就返回
s = re.search(r"\d+", "中国移动：10086，中国电信：10000")
print(s.group())
print("-----")
# match: 从头开始匹配
m = re.match(r"\d+", "10086，中国电信：10000")
print(m.group())
print("-----")

# 预加载正则，可以重复使用
obj = re.compile(r"\d+")

ret = obj.finditer("中国移动：10086，中国电信：10000")
for i in ret:
    print(i.group())
print("-----")
ret = obj.findall("朋友需要还我￥10000")
print(ret)

# 从长字符串中提取特定内容
s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='john'><span id='3'>岳云鹏</span></div>
<div class='peter'><span id='4'>李泽宇</span></div>
<div class='tory'><span id='5'>宋熙鹏</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S)

result = obj.finditer(s)
for it in result:
    print(it.group("wahaha"), end=" ")
    print(it.group("id"))