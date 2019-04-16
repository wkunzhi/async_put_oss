# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-16  Python: 3.7

# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-04-16  Python: 3.7


"""
异步流式上传
"""
import oss2
import time
import aiohttp
import asyncio
import random
import string


# 获取网络流信息
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.read()
    except Exception as e:
        print('访问错误', url)


# 上传
async def put_to(file_name, html, url):
    try:
        obj = bucket.put_object(file_name, html)
        if obj.status == 200:
            print('OK', file_name)
    except Exception as e:
        print('上传错误', url)


# 解析网址
async def pares(url):
    async with aiohttp.ClientSession() as session:
        # 将https更换为http，否则会引起ssl报错问题
        html = await fetch(session, url.replace('https://', 'http://'))
        # 生成随机名，可根据项目不同自行设置
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
        await put_to(salt + '.jpg', html, url)


if __name__ == '__main__':
    key = input('请输入阿里云Key')
    KeySecret = input('请输入阿里云KeySecret')
    endpoint = input('请输入阿里云endpoint')
    bucket_name = input('请输入阿里云bucket_name')

    # oss 认证
    auth = oss2.Auth(key, KeySecret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    tasks = []
    # 统计该爬虫的消耗时间
    t1 = time.time()  # 开始时间

    # 全部网页
    urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d' % i for i in range(1, 26)]

    # 全部加入列队
    for to_url in urls:
        tasks.append(asyncio.ensure_future(pares(to_url)))

    # 利用asyncio模块进行异步IO处理
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(*tasks)
    loop.run_until_complete(tasks)

    t2 = time.time()  # 结束时间
    print('\n使用aiohttp，总共耗时：%s' % (t2 - t1))
