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