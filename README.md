# 网络图片并发直传OSS

![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/ico/python-3.7-green.svg) 
![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/ico/aiohttp-3.5.4-orange.svg)
   ![](https://zok-blog.oss-cn-hangzhou.aliyuncs.com/ico/oss-2-green.svg) 
   
   
| Author  | Zok |
| --- | --- |
| Email | 362416272@qq.com  |
| BLOG | www.zhangkunzhi.com |
   
   -------
   
   ## 无需下载图片
 利用**aiohttp**与**asyncio** 异步上传网络图片，**无需下载**到本地直传服务器
   
   ### 需要配置oss的4个参数
   - key
   - KeySecret
   - endpoint
   - bucket_name
   
   ### 图片URL
   - 网络图片地址需要自己配置