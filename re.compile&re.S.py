import re
#
#
# r2 = re.findall(r'\w*oo\w*',text)
# print(r2)
#
# r = re.compile(r'\w*oo\w*')
# print(r)
#
# r1 = r.findall(text)
# print(r1)
#
# # ['FGood', 'cool']
# # re.compile('\\w*oo\\w*')
# # ['FGood', 'cool']
#
#
# # compile有对规则预编译的作用，它会提高你的编译效率。


# 关于findall加括号的问题
text = "FGood is a handsome boy, he is cool, clever, and so on..."
regex0 = re.compile('\w+\s(\w+)')
r0 = regex0.findall(text)

regex = re.compile('(\w+)\s\w+')
r1 = regex.findall(text)

regex2 = re.compile('\w+\s\w+')
r2 = regex2.findall(text)

regex3 = re.compile('(\w+)\s(\w+)')
r3 = regex3.findall(text)

print(r0)
print(r1)
print(r2)
print(r3)

# ['FGood', 'a', 'he', 'and']
# ['FGood is', 'a handsome', 'he is', 'and so']
# [('FGood', 'is'), ('a', 'handsome'), ('he', 'is'), ('and', 'so')]