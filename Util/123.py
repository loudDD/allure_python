
def decorator(func):
    a = 10
    print("begin wrapper")
    def wrapper():
        print("inner wrapper")
        func()
        print("inner wrapper end")
    print("end wrapper")
    return wrapper

@decorator
def fun():
    print("been wrap")
'''
装饰器可以传参
需要三层
最外层接受参数
第二层接受函数
注意，需要返回两层

'''

def deco(a):
    print("deco" ,a)
    def outer(func):
        print("outer")
        def inner():
            print("inner")
            func()
        return inner
    return outer
@deco(10)
def beg():
    print("begin")


beg()