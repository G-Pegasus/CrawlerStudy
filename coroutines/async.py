import asyncio
import time


async def func1():
    print('你好呀，我叫刘同骥')
    await asyncio.sleep(3)
    print('你好呀，我叫刘同骥')


async def func2():
    print('你好呀，我叫Kana')
    await asyncio.sleep(2)
    print('你好呀，我叫Kana')


async def func3():
    print('你好呀，我叫Pegasus')
    await asyncio.sleep(4)
    print('你好呀，我叫Pegasus')


async def main():
    # 第一种写法
    # f1 = func1()
    # await f1

    tasks = [
        asyncio.create_task(func1()), asyncio.create_task(func2()), asyncio.create_task(func3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)


# 爬虫模板
async def download(url):
    print("准备下载")
    await asyncio.sleep(2)
    print('下载完成')


async def main():
    urls = [
        "https://www.baidu.com"
        "https://www.bilibili.com"
        "https://www.163.com"
    ]

    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())

