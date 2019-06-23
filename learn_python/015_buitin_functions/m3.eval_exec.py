# coding:utf-8
import sys
sys.path.append("../myModules")
from mybasics import blit, show

# 计算字符串表达式
s = "8 * 8"
print(eval(s))

# 执行一个字符串语句
source = '''print("hello world", eval(s))'''
exec(source)

# 执行一个 .py 文件:
with open("./m1.py", 'r') as f:
    exec(f.read())