import requests
import re,json

session = requests.session()  # 会自动保存所有与回话有关的信息    服务端返回的cookie会自动保存session里面
# username = 1861145311
# password = '70621c64832c4d4d66a47be6150b4a8e'
#
# # 第一步:获取登录页面。获取：
# # X-Anit-Forge-Code:77447998
# # X-Anit-Forge-Token:c56c737c-9538-44ba-8ddd-e18163349b06
# # 1：url:https://passport.lagou.com/login/login.html
# # 2：请求方法：get
# # 3: 请求头：
# #   User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
# #   Referer:https://www.lagou.com/lp/html/common.html?utm_source=m_cf_cpc_baidu_pc&m_kw=baidu_cpc_bj_e110f9_d2162e_%E6%8B%89%E5%8B%BE
#
# r1 = session.get('https://passport.lagou.com/login/login.html',
#                  headers={
#                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#                      'Referer': 'https://www.lagou.com/lp/html/common.html?utm_source=m_cf_cpc_baidu_pc&m_kw=baidu_cpc_bj_e110f9_d2162e_%E6%8B%89%E5%8B%BE',
#                  }
#                  )
# X_Anit_Forge_Code = re.findall("X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
# print(X_Anit_Forge_Code)
# X_Anit_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]
#
# # 第二步：
# # 1：url:Request URL:https://passport.lagou.com/login/login.json
# # 2：方法：post
# # 3：
# #   Referer:https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f
# #   User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
# #
# # # 注意了：这里的东西，应该是从之前页面拿过来的对不对 ！
# # X-Anit-Forge-Code:77447998
# # X-Anit-Forge-Token:c56c737c-9538-44ba-8ddd-e18163349b06
# # X-Requested-With:XMLHttpRequest
# # 4、请求体：
# # isValidate:true
# # username:18611453110
# # password:70621c64832c4d4d66a47be6150b4a8e
# # request_form_verifyCode:''
# # submit:''
# """
# 'Referer':'https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f'
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
# 'X-Anit-Forge-Code':77447998
# 'X-Anit-Forge-Token':c56c737c-9538-44ba-8ddd-e18163349b06
# 'X-Requested-With':'XMLHttpRequest'
# """
#
# r2 = session.post('https://passport.lagou.com/login/login.json',
#                   headers={
#                       'Referer': 'https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f',
#                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#                       'X-Anit-Forge-Code': X_Anit_Forge_Code,
#                       'X-Anit-Forge-Token': X_Anit_Forge_Token,
#                       'X-Requested-With': 'XMLHttpRequest'
#                   },
#                   data={
#                       'isValidate': 'true',
#                       'username': username,
#                       'password': password,
#                       'request_form_verifyCode': '',
#                       'submit': ''
#                   }
#                   )
#
# # 第三步： 对已登录用户进行grant授权。
# """
# 1：请求url：https://passport.lagou.com/grantServiceTicket/grant.html
# 2：请求方法：get
# 3：请求头： User-Agent
#           Referer:https://passport.lagou.com/login/login.html
#
# """
#
# r3 = session.get('https://passport.lagou.com/grantServiceTicket/grant.html',
#                  headers={
#                      'Referer': 'https://passport.lagou.com/login/login.html',
#                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#                  })
#
# # 第四步：验证
# r4 = session.get('https://www.lagou.com/resume/myresume.html',
#                  headers={
#                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#                  }
#                  )
# # print(r4.text)
#
# print('18611453110' in r4.text)





# --------------------------->  截止此， 全部是登录验证用。

# ----------------------------------------------->开爬




# 第五步：获取职位信息
# 1：url：https://www.lagou.com/jobs/list_python?px=default&gj=3-5%E5%B9%B4&city=%E5%85%A8%E5%9B%BD
# 2：请求方法：get
# 3：请求头：
#       Referer:https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=
#       Upgrade-Insecure-Requests:1
#       User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

# from urllib.parse import urlencode
# keyword='python开发' # 搜索栏搜索
# # https://www.lagou.com/jobs/list_Python?cl=false&fromSearch=true&labelWords=&suginput=
# url_encode = urlencode({'k':keyword},encoding='utf-8')
# print(url_encode)  # k=python%E5%BC%80%E5%8F%91
# url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput='%url_encode.split('=')[1]
# print(url)   # 根据用户搜索条件，拼接成的url



# r5 = session.get(url,
#                  headers={
#                      'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
#                      'Upgrade-Insecure-Requests': '1',
#                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
#
#                  }
#                  )
# with open('lagou.html','w') as f :
#     f.write(r5.text)

# ！！！！！！！！what the fuck！ 为什么没有我要的信息。
# 发现主页面中并没有我们想要搜索的职位信息，那么肯定是通过后期js渲染出的结果，一查，果然如此
# 搜索职位：请求职位的url后只获取了一些静态内容，关于职位的信息是向https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0发送请求拿到json

# 在XHR里面可看到
# -------------------------------------------------_>


# 第五步不正规，重写
# 第六步:
#   Request URL:https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0
#   Request Method:POST
#   Referer:https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=

# 请求头：
#   User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
#   X-Anit-Forge-Code:0
#   X-Anit-Forge-Token:None
#   X-Requested-With:XMLHttpRequest

# Form Data
#   first:true
#   pn:1
#   kd:python

# params
#   needAddtionalResult:false
#   isSchoolJob:0


# from urllib.parse import urlencode
#
# keyword = 'python开发'  # 搜索栏搜索
# # https://www.lagou.com/jobs/list_Python?cl=false&fromSearch=true&labelWords=&suginput=
# url_encode = urlencode({'k': keyword}, encoding='utf-8')
# print(url_encode)  # k=python%E5%BC%80%E5%8F%91
# url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput=' % url_encode.split('=')[1]
# print(url)
#
# r6 = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',
#                   headers={
#                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#                       'X-Anit-Forge-Code': '0',
#                       'X-Anit-Forge-Token': None,
#                       'X-Requested-With': 'XMLHttpRequest',
#                       'Referer': url
#                   },
#                   data={
#                       'first': True,
#                       'pn': '1',
#                       'kd': keyword
#                   },
#                   params={
#                       'xl': '本科',
#                       'jd': '天使轮',
#                       'px': 'default',
#                       'needAddtionalResult': False,
#                       'isSchoolJob': '1'
#                   })
#
# print(r6.text)








# 终极版：！！！！！！！！！！！！！！！！！

from urllib.parse import urlencode

def get_search(
        keyword,            # 搜索的关键词
        pn=1,
        city='北京',         # 目标城市
        district=None,      # 行政区
        bizArea=None,       # 商圈
        isSchoolJob=None,   # 工作性质
        xl=None,  # 学历
        jd=None,  # 融资阶段
        hy=None,  # 行业
        yx=None,  # 工作范围
        needAddtionalResult=False,
        px='default'
                ):


    # 获取url
    url_encode = urlencode({'k': keyword}, encoding='utf-8')
    print(url_encode)  # k=python%E5%BC%80%E5%8F%91
    url = 'https://www.lagou.com/jobs/list_%s?labelWords=&fromSearch=true&suginput=' % url_encode.split('=')[1]

    r7 = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0',
                      headers={
                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                          'X-Anit-Forge-Code': '0',
                          'X-Anit-Forge-Token': None,
                          'X-Requested-With': 'XMLHttpRequest',
                          'Referer': url
                      },
                      data={
                          'first': True,
                          'pn': pn,
                          'kd': keyword
                      },
                      params={
                          'city': city,  # 工作地点,如北京
                          'district': district,  # 行政区，如朝阳区
                          'bizArea': bizArea,  # 商区，如望京
                          'isSchoolJob': isSchoolJob,  # 工作性质，如应届
                          'xl': xl,  # 学历要求，如大专
                          'jd': jd,  # 融资阶段，如天使轮,A轮
                          'hy': hy,  # 行业领域，如移动互联网
                          'yx': yx,  # 工资范围，如10-15k
                          'needAddtionalResult': needAddtionalResult,
                          'px': px
                      })
    print(r7.status_code)
    print('关于您对<%s职位>的搜索正在进行，请稍后...'%keyword)
    print(r7)
    return r7.json()

# get_search('python开发')

#求职信息
keyword='python开发'
yx='10k-15k'
city='北京'
district='朝阳区'
isSchoolJob='0' #应届或实习

response=get_search(keyword=keyword,yx=yx,city=city,district=district,isSchoolJob=isSchoolJob)
print(response)
results=response['content']['positionResult']['result']
print(results)

#打印公司的详细信息
def get_company_info(results):
    for res in results:
        info = '''
        公司全称 : %s
        地址 : %s,%s
        发布时间 : %s
        职位名 : %s
        职位类型 : %s,%s
        工作模式 : %s
        薪资 : %s
        福利 : %s
        要求工作经验 : %s
        公司规模 : %s
        详细链接 : https://www.lagou.com/jobs/%s.html
        ''' % (
            res['companyFullName'],
            res['city'],
            res['district'],
            res['createTime'],
            res['positionName'],
            res['firstType'],
            res['secondType'],
            res['jobNature'],
            res['salary'],
            res['positionAdvantage'],
            res['workYear'],
            res['companySize'],
            res['positionId']
        )
        print(info)
        # 经分析，公司的详细链接都是：https://www.lagou.com/jobs/2653020.html ，其中那个编号就是职位id
        #print('公司全称[%s],简称[%s]' %(res['companyFullName'],res['companyShortName']))
get_company_info(results)

