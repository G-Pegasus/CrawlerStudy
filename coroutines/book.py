import requests
import asyncio
import aiohttp
import aiofiles
import json


async def aiodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open('novel/' + title, mode="w", encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title'] + ".txt"
        cid = item['cid']
        # 准备异步任务
        tasks.append(aiodownload(cid, b_id, title))

    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = "https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}"
    asyncio.run(getCatalog(url))
