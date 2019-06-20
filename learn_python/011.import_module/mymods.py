import sys
import time

def blit(s):
    for c in s:
        sys.stdout.write(c)
        if c == ' ':
            sys.stdout.flush()
            time.sleep(0.02)
    time.sleep(0.02)


def Foo():
    print("fuction 'foo' running...")

def Bar():
    print("fuction 'bar' running...")