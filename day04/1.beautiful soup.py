#遍历文档树：即直接通过标签名字选择，特点是选择速度快，但如果存在多个相同的标签则只返回第一个
#1、用法
#2、获取标签的名称
#3、获取标签的属性
#4、获取标签的内容
#5、嵌套选择
#6、子节点、子孙节点
#7、父节点、祖先节点
#8、兄弟节点


from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="title"><b>The Dormouse's story</b></p>
<p class="story">...</p>
"""
# 这里使用'lxml'解析器是因为它容错能力强，同时官方也推荐使用lxml解析器。
# 容错能力是指在html代码不完整的情况下，使用该模块可以识别该错误。
# 使用BeautifulSoup解析上述代码，会得到一个 BeautifulSoup对象，并且可以按照标准的缩进格式结构化输出。

soup = BeautifulSoup(html_doc,'lxml')
res = soup.prettify() # 自动补齐所有的未闭合标签。 自己会处理好缩进。
# print(res)

# 遍历文档树：即直接通过标签名字选择，特点是选择速度快，但如果存在多个相同的标签则只返回第一个

# 整个文档中，找到你想要的一个标签。
# print(soup.a)  # .的话，是按标签名查找。 只找第一个
# print(soup.a.text) # 文本
# print(soup.a.attrs) # 所有属性，是字典格式
# print(soup.p.b)  # p下面的儿子，孙子，重孙子 一层层找，只找一个
# print(soup.p.contents)  # 将所有儿子放在一个列表里
# print(soup.p.children) # 生成器
# print(list(soup.p.children))
# print(list(soup.p.descendants)) # 子子孙孙  也是生成器
#
# print(soup.a.parent) #  塔爹
# # print(list(soup.a.parents)) # 找到a标签所有的祖先节点，父亲的父亲，父亲的父亲的父亲...

print(soup.a.next_sibling)      # 下一个兄弟
print(soup.a.previous_sibling)  # 上一个兄弟

print(list(soup.a.next_siblings))     # 下面的兄弟们，返回的是一个生成器对象
print(list(soup.a.previous_siblings)) # 上面的兄弟们，返回的是一个生成器对象


"""
输出结果：
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
Elsie
{'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
None
['Once upon a time there were three little sisters; and their names were\n', <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, ',\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, ';\nand they lived at the bottom of a well.']
<list_iterator object at 0x1025b15c0>
['Once upon a time there were three little sisters; and their names were\n', <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, ',\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, ';\nand they lived at the bottom of a well.']
['Once upon a time there were three little sisters; and their names were\n', <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 'Elsie', ',\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 'Lacie', ' and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, 'Tillie', ';\nand they lived at the bottom of a well.']
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>


,

Once upon a time there were three little sisters; and their names were

[',\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, ';\nand they lived at the bottom of a well.']
['Once upon a time there were three little sisters; and their names were\n']

"""