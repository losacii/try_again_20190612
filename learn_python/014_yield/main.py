# coding: utf-8
import sys

print( range(10) )
print( xrange(10) )

for i in xrange(5):
    print(i)

''' xrange 只有在遍历的时候,才一个一个生成;
    延迟生成数据;
    类似有: xreadlines()
'''

def foo():
    yield 3
    yield 4
    yield 5

x = foo() # generator

print(x)  # print generator

for i in x: # 遍历 generator
    print(i)

# ---------------------------------------

fp = "../FILES/lorem_ipsum.txt"

def xfile(filepath):
    seek = 0
    while True:
        with open(filepath, 'r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                yield data
                seek = f.tell()
            else:
                return
        
for line in xfile(fp):
    sys.stdout.write(line)