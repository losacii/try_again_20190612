# coding:utf-8
''' ~~~~~~~~~> Regular Expression
# match, search, findall, compile, group, groups
'''
import re


needle = "\d+"
haystack = "what2idsf93hu*38329"

result = re.search(needle, haystack)
results = re.findall(needle, haystack)
print(result.group())
print(results)

# group()
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group())     #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))     #123abc456,返回整体

print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))    # 第1括号
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))     # 第2括号
print (re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))     # 第3括号

# compile
patt = re.compile("\d+")
print( patt.findall("what2idsf93hu*38329") )

# group & groups
# https://blog.csdn.net/chr1991/article/details/80945455
# 30分钟 正则表达式 教程
'''
group和groups是两个不同的函数。
一般，m.group(N) 返回第N组括号匹配的字符。
而m.group() == m.group(0) == 所有匹配的字符，与括号无关，这个是API规定的。

m.groups() 返回所有括号匹配的字符，以tuple格式。
m.groups() == (m.group(0), m.group(1), ...)
'''




''' ~~~~~~~~~> result
'''