
def sum(*args):
    x = 0
    for i in args:
        x += i
    return x

v = sum(2, 3, 5, 9, 7);  print(v)
    

def show(**kargs):
    for item in kargs.items():
        print(item)        


show(name="Alex", gender="Male", career="Scientist", age=55)

'''
    1个星, 后面的名称, 是一个 列表
    2个星, 后面的名称, 是一个 字典
'''