# 遍历文档树：即直接通过标签名字选择，特点是选择速度快，但如果存在多个相同的标签则只返回第一个

import re
from bs4 import BeautifulSoup
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">...</p>
# """
#
#
# soup = BeautifulSoup(html_doc,'lxml')
# res = soup.prettify()



# 一：五种过滤器：字符串，正则表达式，列表，True,方法

# 1：字符串过滤器 # 标签名
# print(soup.find())  # 全部
# soup.find_all(name='a')  # 找所有的标签,  使用字符串匹配标签名。  特点：完全匹配
# soup.find_all(attrs={'class':'sister'})  # 找所有的标签,  使用字符串匹配标签名。  特点：完全匹配
# print(soup.find_all(name='b',text="Dormouse"))    # 匹配不到，因为text不完整。不能模糊匹配。

# # 2：正则
# soup.find_all(name=re.compile('^b'))  # compile 编译   按标签查找
# soup.find_all(attrs={'id':re.compile('link')})  # compile 编译

# 3：列表过滤器列表：   任意一个标签都会返回
# 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.
# 下面代码找到文档中所有<a>标签和<b>标签:
# print(soup.find_all(['a','b']))

# 4：True：可以匹配任何值，会查找到所有的tag，但是不会返回字符串节点。
# print(soup.find_all(True))
# for tag in soup.find_all(True):
    # print(tag.contents)
    # print(tag.text)
    # print(tag)
# 5：方法
# 用于没有找到合适过滤器，就可以定义一个方法，方法只接受一个元素参数。
# 如果该方法，返回一个True，表示当前元素被匹配并被找到，如果不是则返回False。
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_but_no_id))
"""
has_class_but_no_id:
[<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>, <p class="title"><b>The Dormouse's story</b></p>, <p class="story">...</p>]
"""

# recursive = True  # 当前标签下的子子孙孙
# recursive = False # 当前标签下的儿子

# 二：find_all(name,attrs,recursive,text,**kwargs)

# 2.1 name参数是可以使用任何一种类型的过滤器，（字符串，True，正则，列表）
# print(soup.find_all(name=re.compile('^t')))

# 2.2 keyword：key=value格式, value可以是过滤器（字符串，True，正则，列表）。
# print(soup.find_all(id=re.compile('my')))
# print(soup.find_all(href=re.compile('lacie'),id=re.compile('\d'))) #注意类要用class_
# print(soup.find_all(id=True)) #查找有id属性的标签
# 2.2.1 注意事项：！！
# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>','lxml')
# data_soup.find_all(data-foo="value") #报错：SyntaxError: keyword can't be an expression
# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
# print(data_soup.find_all(attrs={"data-foo": "value"}))
# [<div data-foo="value">foo!</div>]

# 2.3 按照类名查找，注意关键字是class_，class_=value,value可以是五种选择器之一
# print(soup.find_all('a',class_='sister')) #查找类为sister的a标签
# print(soup.find_all('a',class_='sister ssss')) #查找类为sister和sss的a标签，顺序错误也匹配不成功
# print(soup.find_all(class_=re.compile('^sis'))) #查找类为sister的所有标签

# 2.4 attrs
# print(soup.find_all('p',attrs={'class':'story'}))

# 2.5 text: 值可以是：字符，列表，True，正则
# print(soup.find_all(text='Elsie'))
# print(soup.find_all('a',text='Elsie'))
#
# # 2.6 limit参数:如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果
# print(soup.find_all('a',limit=2))
#
# # 2.7 recursive:调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
# print(soup.html.find_all('a'))
# print(soup.html.find_all('a',recursive=False))

'''
像调用 find_all() 一样调用tag
find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. 
BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:
soup.find_all("a")
soup("a")
这两行代码也是等价的:
soup.title.find_all(text=True)
soup.title(text=True)
'''


# 三：find(name , attrs , recursive , text , **kwargs)
# 你可能会想，既然已经有了find_all()了，我干嘛还要find。
# find_all() 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.
# 比如文档中只有一个<body>标签,那么使用 find_all() 方法来查找<body>标签就不太合适,
# 使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法.下面两行代码是等价的:

# soup.find_all('title', limit=1)
# [<title>The Dormouse's story</title>]
# soup.find('title')
# <title>The Dormouse's story</title>

# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.
# find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .
# print(soup.find("nosuchtag"))
# None

# soup.head.title 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 find() 方法:
#
# soup.head.title
# <title>The Dormouse's story</title>
# soup.find("head").find("title")
# <title>The Dormouse's story</title>


# 四：css选择器
# 该模块提供了select方法来支持css。
#该模块提供了select方法来支持css,
# 详见官网:https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id37

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">
    <b>The Dormouse's story</b>
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
        <span>Elsie</span>
    </a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    <div class='panel-1'>
        <ul class='list' id='list-1'>
            <li class='element'>Foo</li>
            <li class='element'>Bar</li>
            <li class='element'>Jay</li>
        </ul>
        <ul class='list list-small' id='list-2'>
            <li class='element'><h1 class='yyyy'>Foo</h1></li>
            <li class='element xxx'>Bar</li>
            <li class='element'>Jay</li>
        </ul>
    </div>
    and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,'lxml')
# 4.1 CSS选择器
# print(soup.p.select('.sister'))           # 找类名为sister的标签
# print(soup.select('.sister span'))        # 找类名为sister的标签下面的span标签

# print(soup.select('#link1'))              # 找id为link1的标签
# print(soup.select('#link1 span'))         # 找id为link1的标签下面的span标签
#
print(soup.select('#list-2 .element.xxx'))# 找id为link-2的标签下面的类名为element xxx的标签
#
# print(soup.select('#list-2')[0].select('.element')) #可以一直select,但其实没必要,一条select就可以了
#
# # 4.2 获取属性
# print(soup.select('#list-2 h1')[0].attrs)
#
# # 4.3 获取内容
# print(soup.select('#list-2 h1')[0].get_text())



# 总结:
#1、推荐使用lxml解析库
#2、讲了三种选择器:标签选择器,find与find_all，css选择器
    # 1、标签选择器筛选功能弱,但是速度快
    # 2、建议使用find,find_all查询匹配单个结果或者多个结果
    # 3、如果对css选择器非常熟悉建议使用select
#3、记住常用的获取属性attrs和文本值get_text()的方法