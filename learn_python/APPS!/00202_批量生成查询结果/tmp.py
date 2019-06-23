# coding: utf-8
"""
    输入数据格式化
"""
import sys

def m1():
    # stdin
    str_list = []
    for line in sys.stdin:
        if line.strip() == "\\e":
            break
        tmpStr = line.split()
        str_list.extend(tmpStr)

    print(str_list)

def m2():
    # input()
    lines = []
    while True:
        try:
            lines.append(input())
        except:
            break
    print(lines)

def m3():
    # readlines()
    lines = sys.stdin.readlines()
    print(lines)


if __name__ == "__main__":
    m3()