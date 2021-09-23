# 默认值参数
# 我们创建一个函数，定义参数中一个或多个赋予默认值后，我们可以使用比允许的更少的参数去调用此函数

def def_param_fun(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#print(def_param_fun('请输入的参数 \n',5,'yes'))

#我们可以使用一个或多个参数去调用此函数，我们实际生产中,很多情况下会赋予函数参数默认值的情形，因此，合理使用此种参数形式可以简化我们很多工作量

#重要：使用默认值参数时，如果我们的默认值是一个可变对象时，我们调用函数可能出现不符合我们预期的结果
def f(a, l=[]):
    l.append(a)
    return l

#print(f(1))
#print(f(2))
#print(f(3))

#这是由于函数在初始化时，默认值只会执行一次，所以在默认值为可变对象（列表、字典以及大多数类实例）
def f1(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f1(1))
print(f1(2))
print(f1(3))

def variable_fun(kind, *arguments, **keywords):
    #*arguments 可以传入列表 元组
    #**keywords 可以传入字典
    print("friend : ", kind, ";")
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

variable_fun('kind',[1,2,3,4,5],{"Apple":15,"kiwifruits":115})

#关键字参数

#关键字参数允许你调用函数时传入0个或任意个含参数名的参数，这样可以让我们灵活的去进行参数的调用
def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This key_fun wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 函数调用  
key_fun(1000)                                          # 1 positional argument
key_fun(voltage=1000)                                  # 1 keyword argument
key_fun(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
key_fun(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
key_fun('a million', 'bereft of life', 'jump')         # 3 positional arguments
key_fun('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword