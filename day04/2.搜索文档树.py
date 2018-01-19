import re
from bs4 import BeautifulSoup

soup = BeautifulSoup()


# 五种过滤器
# 1：字符串过滤器
soup.find()      #
soup.find_all(name='a')  # 找所有的标签,  使用字符串匹配标签名。  特点：完全匹配
soup.find_all(attrs={'class':'sister'})  # 找所有的标签,  使用字符串匹配标签名。  特点：完全匹配
soup.find_all(name='b',text='I Love You')

# 2：正则
soup.find_all(name=re.compile('b'))  # compile 编译   按标签查找
soup.find_all(attrs={'id':re.compile('link')})  # compile 编译

# 3：列表过滤器


# 4：True

# 5：方法




recursive = True  # 当前标签下的子子孙孙
recursive = False # 当前标签下的儿子