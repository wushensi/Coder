# 装饰器 简化了代码，在返回一个新的函数，保留了原函数，扩张了新功能
#def IAmDecorator(foo):
#    '''我是一个装饰函数'''
#    print('extend function')
#    return foo
#
#@IAmDecorator
#def tobeDecorated():
#    '''我是被装饰函数'''
#    print('original function')


#def IAmFakeDecorator(fun):
#    print("我是一个假的装饰器")
#    return fun
#
#@IAmFakeDecorator
#def func():
#    print("我是原函数")

def IAmFakeDecorator(fun):
    def wrapper(*args,**kw):
        print("我是一个真的装饰器")
        return fun(*args,**kw)
    return wrapper

@IAmFakeDecorator
def func():
    print("我是原函数")

@IAmFakeDecorator
def func1(h):
    print("我是原函数1")

#tobeDecorated()
#tobeDecorated()
#tobeDecorated()

#func()
#func()
#func()

func()
func()
func()

func1(1)

print(func.__name__) # 函数名称却变成了装饰器中内部函数的名称。

import functools # 保留原函数名称

def IAmDecoratorKeepFunName(fun):
    @functools.wraps(fun) #functools.wraps 也是装饰器
    def wrapper(*args,**kw):
        print("我是一个真的装饰器 functools")
        return fun(*args,**kw)
    return wrapper

@IAmDecoratorKeepFunName
def func2():
    print("我是原函数 functools")

func2()

print(func2.__name__)
