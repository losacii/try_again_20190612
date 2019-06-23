# coding:utf-8

# map函数, 接收 函数名 和 一个序列, 返回 经过函数的序列--> 是个map对象, 生成器
li = [1, 2, 3, 4, 5, 6, 7]
def func(x):
    return x * x + 100
ly = map(func, li)

for i in ly:
    print(i)

# filter(func, li)
# ---> eg1
x = filter(lambda x:x > 10, [13, 5, 7, 11, 9, 22])
for i in x:
    print('-->', i) # 13, 11, 22

# ---> eg2
li = [13, 5, 7, 11, 9, 22]
def func(x):
    return x > 10
x = filter(func, li)
for i in x:
    print('-->', i) # 13, 11, 22

# reduce
from functools import reduce
li = [8, 5, 9, 2, 3, 17]
print(reduce(lambda x, y : x * y, li))