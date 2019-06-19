# coding:utf-8

# ord() chr()
print(ord('A'), ord('Z'))
print(ord('a'), ord('z'))

# decode to unicode, encode from unicode
'''
    ascii: 2 ** 8 --> 256
    unicode: 2**16 --> 25536
    utf-8: 可变长度，3字节， 2**24 --->
'''

# unicode
a = u'alex'
print(type(a))

name = u'你好'
print(name, type(name))