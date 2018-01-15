import requests
import re


# 第一步:获取登录页面，拿到authenticity_token.GYWXO/m52XooAkyOqWQtk16Nuxk8E4XQ1tOEXMjm5bRPd8XDHTQgQ/G4Y0mpqL3Uax0LjQ33vN7hMh1otO7Btg==
# 1:请求的url：https://github.com/login
# 2:请求方式：get
# 3:请求头：User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
r1 = requests.get('https://github.com/login',
                  headers={
                      'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                  },)

# 获取authenticity_token
# 这里有疑问，为什么要用findall
authenticity_token = re.findall('name="authenticity_token".*?value="(.*?)"',r1.text,re.S)[0]
# 获取cookie 这里有简单方法
r1_cookies = r1.cookies.get_dict()
print(authenticity_token)
print(r1_cookies)


# 第二步:提交表单数据，完成登录
# 1:请求的url：https://github.com/session
# 2:请求方式：post
# 3.1:这里因为是post请求，所以这步要注意请求头，请求体
    # 关于头
    # Referer:https://github.com/
    # User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

# 3.2 关于体
# commit:Sign in
# utf8:✓
# authenticity_token:GYWXO/m52XooAkyOqWQtk16Nuxk8E4XQ1tOEXMjm5bRPd8XDHTQgQ/G4Y0mpqL3Uax0LjQ33vN7hMh1otO7Btg==
# login:66666666
# password:666666

r2 = requests.post('https://github.com/session',
                   headers={
                       'Referer':'https://github.com/',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                   },
                   cookies = r1_cookies,
                   # 请求体相关data
                   data={
                        'commit': 'Sign in',
                       'utf8': '✓',
                       'authenticity_token': authenticity_token,
                       'login': 'ugfly@qq.com',
                       'password': 'fei19921210'
                   },
                    # allow_redirects=False
                   )

print(r2.status_code)
print(r2.history)

r2_cookies = r2.cookies.get_dict()
print(r2_cookies)
print(r2.cookies)


r3=requests.get('https://github.com/settings/emails',
             headers={
                 "Referer": "https://github.com/",
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
             },
             cookies=r2_cookies)
print('ugfly@qq.com' in r3.text)

