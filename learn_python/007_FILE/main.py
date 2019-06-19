# coding:utf-8
import time

# - - - - - - - - - - - open file - - - - - - - - - - - 
fp = open("lorem.txt")

print(dir(fp))

print(fp.encoding)

# 打印所有行
for line in fp:
    line = line.strip().upper()
    print(line)

fp.seek(0) # 文件指针回到开始位置
# 读取固定长度
print(fp.read(10))
print(fp.read(10))
print(fp.read(10))

# 显示当前指针位置
print(fp.tell()) # tell current position


# 读取固定长度，直到结束
fp.seek(0)
while True:
    content = fp.read(100)
    if content:
        print("\n-->", content)
    else:
        print("====> position:", fp.tell())
        break

# - - - - - - - - - - - close file - - - - - - - - - - - 
fp.close()