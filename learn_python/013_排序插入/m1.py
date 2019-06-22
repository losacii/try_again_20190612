# coding: utf-8
"""
    用跳转法: 快速把单个数值插入列表中,形成新的有序列表;
"""
import math
import time
import sys
put = sys.stdout.write

def foo(x, li):
    index = 0
    jump = math.ceil( len(li) / 2 )

    while True:
        put("\n\n----> jump index: {} with {}".format(index, jump))
        index += jump
        time.sleep(1)

        # 到达边界
        if index > len(li) - 1 or index < 1:
            put("{}: reach to boundary".format(index))
            li.insert(index, x)
            return li

        # x 比 取值 小, 两种情况
        if x < li[index]:
            put("\n{} is less than {}".format(x, li[index]))
            if x > li[index-1]:
                put(", and {} is greater than {} ==>\n".format(x, li[index-1]))
                li.insert(index, x)
                return li
            else:
                jump = -math.ceil( abs(jump / 2) )

        # x 比 取值 大, 两种情况
        elif x > li[index]:
            put("\n{} is greater than {}".format(x, li[index]))
            if x < li[index + 1]:
                put(", and {} is less than {} ==>\n".format(x, li[index+1]))
                li.insert(index+1, x)
                return li
            else:
                jump = math.ceil( abs(jump / 2) )

        # x 等于 取值, 一种情况
        else:
            li.insert(index, x)
            return li

if __name__ == "__main__":
    print(__doc__)

    li = ['a', 'd', 'j', 'k', 'l', 't', 'z']
    x = 'y'
    print(foo(x, li))   