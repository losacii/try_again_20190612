'''
    help(), dir(), vars()
    type()
    import, reload
    id()
'''

# enumerate, help(enumerate)
products = ['car', 'house', 'TV', 'telephone']
for i in enumerate(products, start=5):
    print(i)

# vars() --> help(vars)
print(vars())

# from module import demo
# reload(demo)

x = 5
y = 8
print(id(x), id(y))

"""
    cmp(3, 5)
    abs(-3.7)
    divmod(), 浏览器分页应用
    max(), min()
    sum()
    pow()
    len()
    all(), any()
"""
print(divmod(13, 5))
print(max([6, 2, 5, 9, 7, 3, 3]))

print(pow(2, 10))
print( 2**(1/2), 5**(1/2) )

x = all([1,2,3,4,0]); print(x)
x = all([1,2,3,4,1]); print(x)

# chr, ord, 生成随机验证码
print(ord('A'), ord('a'))
print(chr(12), chr(66))

# hex, oct, bin
x = [
    hex(33),
    oct(17),
    bin(15)
];  print(x)

# range, xrange

# enumerate, help(enumerate)
li = ['car', 'house', 'tv', 'computer', 'watch']
for i in enumerate(li, start=5):
    print(i)

# string formatting
s = "I am {}, {}"
print( s.format("Alex", "Hello There!") )
