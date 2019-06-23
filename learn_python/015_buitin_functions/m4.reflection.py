# coding:utf-8
import sys
sys.path.append("../myModules")
from mybasics import blit, show

# 反射: 以字符串的形式, 导入模块|执行函数

source = 'os'
func = 'getcwd'

model = __import__(source)
function = getattr(model, func)

print("-------->")
function()
print("-------->")
print(function())