import time
import sys
import os

def blit(s):
    for c in s:
        sys.stdout.write(c)
        if c == ' ':
            sys.stdout.flush()
            time.sleep(0.02)
    time.sleep(0.02)

lines = open("lorem.txt").readlines()

# for _ in range(3):

#     os.system("cls")
#     time.sleep(1)

#     for line in lines:
#         blit(line)
#     time.sleep(3)


for _ in range(3):
    blit("\rhello world")
    time.sleep(0.5)