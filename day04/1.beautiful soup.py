from bs4 import BeautifulSoup

soup = BeautifulSoup()
soup.prettify() # 自动补齐所有的未闭合标签

# 整个文档中，找到你想要的一个标签。
print(soup.a)  # .的话，是按标签名查找。 只找第一个
print(soup.a.text) # 文本
print(soup.a.attrs) # 所有属性，是字典格式
print(soup.p.b)  # p下面的儿子，孙子，重孙子 一层层找，只找一个
print(soup.p.contents)  # 将所有儿子放在一个列表里
print(soup.p.children) # 生成器
print(list(soup.p.descendants)) # 子子孙孙  也是生成器

print(soup.a.parent) #  塔爹
print(list(soup.a.parents)) # 它所有的爹
print()



##########搜索树
soup.p.find()