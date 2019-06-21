
def sum(*args):
    '传入列表'
    print("~ " * 16)
    x = 0
    for i in args:
        x += i
    return x

# 调用方式1
v = sum(2, 3, 5, 9, 7);  print(v)

# 调用方式2
li = [4, 6, 9, 8]
print(sum(*li))
    

def show(**kargs):
    '传入字典'
    print("~ " * 16)
    for item in kargs.items():
        print(item)        


# 调用方式1
show(name="Alex", gender="Male", career="Scientist", age=55)

# 调用方式2
dx = {"name": "Alex", "gender": "Male", "career": "Scientist", "age": 55}
show(**dx)

'''
    1个星, 后面的名称, 是一个 列表
    2个星, 后面的名称, 是一个 字典
'''