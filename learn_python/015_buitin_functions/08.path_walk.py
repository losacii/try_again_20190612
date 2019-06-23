# coding:utf-8
import os

print(" dirs ".center(80, '~'))
for root, dirs, files in os.walk("../", topdown=False):
    for dirname in dirs:
        print(os.path.join(root, dirname))

print(" files ".center(80, '~'))
for root, dirs, files in os.walk("../", topdown=False):
    for file_name in files:
        print(os.path.join(root, file_name))

'''
从上面可以看出, walk 返回: 
    root 是字符串
    dirs 是列表
    files 是列表
'''