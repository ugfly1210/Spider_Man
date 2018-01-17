# 一：证书验证
    # 加参数：   cert=('/path/server.crt',
#                     '/path/key')



# 二：代理  ***
# #代理设置:先发送请求给代理,然后由代理帮忙发送(封ip是常见的事情)
#   2.1  import requests
#                 先来一个字典，存代理信息
#                 {'http':'代理主机的ip:port'}
# proxies={
#     'http':'http://878:123@localhost:9743',#带用户名密码的代理,@符号前是用户名与密码
#     'http':'http://localhost:9743',
#     'https':'https://localhost:9743',
# }
# response=requests.get('https://www.12306.cn',
#                      proxies=proxies)
#
# print(response.status_code)
#
#
#   2.2  该代理不依赖于具体协议，什么样的请求都可以交给它转发。
# #支持socks代理,安装:pip install requests[socks]
# import requests
# proxies = {
#     'http': 'socks5://user:pass@host:port',
#     'https': 'socks5://user:pass@host:port'
# }
# response=requests.get('https://www.12306.cn',
#                      proxies=proxies)***
#
# print(response.status_code)




# 三：超时时间 ***   timeout
import requests
#两种超时:float or tuple
#timeout=0.1 #代表接收数据的超时时间
#timeout=(0.1,0.2)#0.1代表链接超时  0.2代表接收数据的超时时间
response = requests.get('https://www.baidu.com',
                        timeout=1.1) # 代表请求和服务端返回数据的总时间
                                     # 这里如果想单独控制链接时间和响应时间，就写成元组形式就好。


# 四：认证设置
#

# 五：异常处理 requests里面自带的有一些异常 ***



# 六：上传文件   files = '文件句柄'