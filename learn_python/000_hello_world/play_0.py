import os
import sys
import time

while True:
    os.system("cls"); time.sleep(1)
    for ch in "hello world!":
        sys.stdout.write("    " + ch+'\n')
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(3)
