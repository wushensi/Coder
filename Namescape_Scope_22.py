# 命名空间 局部变量、全局变量、内置变量
# 作用域关键字 global nonlocal

'''Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问'''
name1 = 'abc'
if chr('abc'.__eq__(name1)):
    result = 'I am from a'
else:
    result = 'I am from b'

print(result)
print(type(result))

def callName():
    name2 = 'abc'
    if chr('abc'.__eq__(name1)):
        result = 'I am from a'
    else:
        result = 'I am from b'

#print(name2) #无法识别 会抛出NameError 异常

total = 0
def sum(a,b):
    total= a+b
    return total
print(sum(1,50))
print(total)

# 修改全局变量 使用global关键字
numberg = 1

def fun1():
    global numberg #需要使用global关键字声明
    print(numberg)
    numberg = 111
    print(numberg)

print('unchange---',numberg) #未修改的全局变量
fun1() #声明使用全局遍历，调用处理全局遍历
print('changed---',numberg) #内部函数调用修改全局变量

# 修改嵌套作用域
def outer():
    numberL=10
    print('unchanged ---', numberL)
    def inner():
        nonlocal numberL #nonlocal 关键字声明，使用函数变量
        numberL = 1000
        print('changed --- ',numberL)
    inner() #内部函数调用处理
    print('outer ---',numberL)

outer()

