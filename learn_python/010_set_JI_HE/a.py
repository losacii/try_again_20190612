# coding: utf-8

# eg1: add
s = set()

s.add(1)
s.add(3)
s.add(5)
s.add(3)
s.add(9)

# eg 2: operators
a = {5, 1, 3, 4, 3, 6, 9}
b = {2, 3, 3, 17}

print(a | b)
print(a - b)

print(a & b)   # 交集
print(a ^ b)   # 并集 - 交集

# eg: 3: update with:  list / tuple / dict
c = set('hello')
c.update("world")
print(c)

"""
    'add',
    'clear',
    'copy',
    'difference',
    'difference_update',
    'discard',
    'intersection',
    'intersection_update',
    'isdisjoint',
    'issubset',     包含于
    'issuperset',   包含
    'pop',
    'remove',       移除
    'symmetric_difference',
    'symmetric_difference_update',
    'union',  合并
    'update'  扩充
"""