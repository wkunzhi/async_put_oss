# 网络图片并发直传OSS

   
| Author  | Zok |
| --- | --- |
| Email | 362416272@qq.com  |
| BLOG | www.zhangkunzhi.com |
   
   -------
   
   # 逻辑
   > 利用redis列队形式，批量上传图片到oss中, 从列队左侧弹出url并上传url，如果上传失败，则右侧重新推入url
   ## 无需下载图片
 线程模式批量上传图片，**无需下载**到本地直传服务器
   
   ### 需要配置oss的4个参数
   - key
   - KeySecret
   - endpoint
   - bucket_name
   
   ### 图片URL
   - 网络图片地址需要自己配置
   
   