# coding: utf-8
""" lambda : 匿名函数, 没有名称, 用于简单调用 """

temp = lambda x, y : x * y + y
print(temp(5, 8))

# 生成列表的一种方式
li = [x * 2 for x in range(8)]
print(li)

# map, lambda结合使用
mapobj = map(lambda x,y : x*y+y, range(5), range(5,10))
print(list(mapobj))