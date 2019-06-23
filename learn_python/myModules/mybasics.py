# coding:utf-8
import os
import sys
import time

def blit(value):
    for ch in str(value):
        sys.stdout.write(ch)
        if ch == ' ':
            sys.stdout.flush()
            time.sleep(0.02)
    time.sleep(0.02)

def show(s):
    for i in s:
        print(i)

if __name__ == "__main__":
    blit("hello world")
    show([3,4,5,"hello"])
