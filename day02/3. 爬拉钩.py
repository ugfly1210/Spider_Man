# 未封装版
import requests
import re
import json
from urllib.parse import urlencode

session = requests.session()  # 会自动保存所有与回话有关的信息    服务端返回的cookie会自动保存session里面
username = 666
password = '70621c64832c4d4d66a47be6150b4a8e'

# 一
r1 = session.get('https://passport.lagou.com/login/login.html',
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                     'Referer': 'https://www.lagou.com/lp/html/common.html?utm_source=m_cf_cpc_baidu_pc&m_kw=baidu_cpc_bj_e110f9_d2162e_%E6%8B%89%E5%8B%BE',
                 }
                 )
X_Anti_Forge_Code = re.findall("X_Anti_Forge_Code = '(.*?)'", r1.text, re.S)[0]
print(X_Anti_Forge_Code)
X_Anti_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", r1.text, re.S)[0]

# 二
r2 = session.post('https://passport.lagou.com/login/login.json',
                  headers={
                      'Referer': 'https://passport.lagou.com/login/login.html?service=https%3a%2f%2fwww.lagou.com%2f',
                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                      'X-Anti-Forge-Code': X_Anti_Forge_Code,
                      'X-Anti-Forge-Token': X_Anti_Forge_Token,
                      'X-Requested-With': 'XMLHttpRequest'
                  },
                  data={
                      'isValidate': 'true',
                      'username': username,
                      'password': password,
                      'request_form_verifyCode': '',
                      'submit': ''
                  }
                  )

# 第三步： 对已登录用户进行grant授权。
r3 = session.get('https://passport.lagou.com/grantServiceTicket/grant.html',
                 headers={
                     'Referer': 'https://passport.lagou.com/login/login.html',
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                 })

# 第四步：验证
r4 = session.get('https://www.lagou.com/resume/myresume.html',
                 headers={
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                 }
                 )
# print(r4.text)

print('显示是否登录成功。如果成功True，否则：False  ------------->',username in r4.text)


session = requests.session()
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
                          'X-Anti-Forge-Code': '0',
                          'X-Anti-Forge-Token': None,
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
    print('关于您对<%s职位>的搜索正在进行，请稍后...'%keyword)
    print(r7)
    return r7


# 打印公司的详细信息
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
        # with open('招聘信息','w') as f :
        #     f.write(info)
        print(info)
        # 经分析，公司的详细链接都是：https://www.lagou.com/jobs/2653020.html ，其中那个编号就是职位id
        #print('公司全称[%s],简称[%s]' %(res['companyFullName'],res['companyShortName']))

# get_company_info(results)




# 投简历
def throw_resumes():
    rr = json.dumps(response)
    X_Anti_Forge_Code = re.findall("X_Anti_Forge_Code = '(.*?)'", rr.text, re.S)[0]
    print(X_Anti_Forge_Code)
    X_Anti_Forge_Token = re.findall("X_Anti_Forge_Token = '(.*?)'", rr.text, re.S)[0]

    for res in results:
        positionId = res['positionId']
        company_link = 'https://www.lagou.com/jobs/{pos_id}.html'.format(pos_id=positionId)
        session.post('https://www.lagou.com/mycenterDelay/deliverResumeBeforce.json',
                     headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                         'Referer': company_link,
                         'X-Anti-Forge-Code': X_Anti_Forge_Code,
                         'X-Anti-Forge-Token': X_Anti_Forge_Token,
                         'X-Requested-With': 'XMLHttpRequest'
                     },
                     data={
                         'positionId': positionId,
                         'type': 1,
                         'force': True
                     })



#======================================over

# 输入求职信息
keyword = 'python'
yx = '5k-25k'
city = '西安'
district = '不限'
isSchoolJob = '0'  # 应届或实习

response = get_search(keyword=keyword, yx=yx, city=city, district=district, isSchoolJob=isSchoolJob).json()
print(response)
results = response['content']['positionResult']['result']
print(results)
get_company_info(results)


# 不需要投简历时，请注释掉！！！
throw_resumes()