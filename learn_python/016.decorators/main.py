# coding:utf-8
import sys
sys.path.append("../myModules") # 
from mybasics import blit, show

# blit("hello world")
# show([3,4,5,"hello"])


def just_an_outer(func):
    def wrapper():
        blit("\n" + " Function Started! ".center(80, "~"))
        func()
        print(" Function Stopped! ".center(38, "~"), "\n\n")
    return wrapper


@just_an_outer
def foo():
    for i in range(3):
        print("foo!")

@just_an_outer
def bar():
    for i in range(3):
        print("bar!")

if __name__ == "__main__":
    foo()
    bar()