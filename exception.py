#SyntaxError: invalid syntax
#while True print('this is python')
#if 1=1:
#    print(True)

# exception 
# TypeError exception
#a='1'+2
#print(a)

# try...except...else 为例：
#1、首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）。
#2、如果没有异常发生，则跳过 except 子句 并完成 try 语句的执行。
#3、如果在执行try 子句时发生了异常，则跳过该子句中剩下的部分。然后，如果异常的类型和 except 关键字后面的异常匹配，则执行 except 子句，然后继续执行 try 语句之后的代码。
#4、如果发生的异常和 except 子句中指定的异常不匹配，则将其传递到外部的 try 语句中；如果没有找到处理程序，则它是一个 未处理异常，执行将停止并显示错误消息。
#5、如果 try 语句执行时没有发生异常，那么将执行 else 语句后的语句（如果有 else 的话），然后控制流通过整个 try 语句。

class BException(Exception):  #继承Exception基类
    pass

class CException(BException):  #继承BException基类
    pass

class DException(CException):  #继承CException基类
    pass


for cls in [BException, CException, DException]:
    try:
        raise cls()  #抛出异常
    except DException:
        print("D")
    except CException:
        print("C")
    except BException:
        print("B")

#如果 except 子句被颠倒（把 except BException 放到第一个），它将打印 B，B，B --- 因为DException类继承CException类，CException类继承BException类，将 except BException 放到第一个可以匹配这三个异常，后面的 except 就不会执行。
for cls in [BException, CException, DException]:
    try:
        raise cls()  #抛出异常
    except BException:
        print("B")
    except DException:
        print("D")
    except CException:
        print("C")

#Python可以在所有 except 的最后加上 except 子句，这个子句可以省略异常名，以用作通配符。它可以捕获前面任何 except （如果有的话）没有捕获的所有异常。
try:
    raise BException()  #抛出异常
except DException:
    print("D")
except:
    print("处理全部其它异常1") #处理全部其它异常

#一个 try 语句可能有多个 except 子句，以指定不同异常的处理程序，最多会执行一个处理程序。处理程序只处理相应的 try 子句中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。一个 except 子句可以将多个异常命名为带括号的元组。
try:
    #raise BException()  #抛出异常
    pass
except (BException, DException):
    print("D")
except:
    print("处理全部其它异常2") #处理全部其它异常
else:
    print("没有异常发生") #没有异常发生

#这里注意 finally 和 else 的区别，finally 是无论是否有异常都会执行，而 else 语句只有没有异常时才会执行。也就是说如果没有异常，那么 finally 和 else 都会执行。
try:
    raise BException()  #抛出异常
except (BException, DException):
    print("D")
except:
    print("处理全部其它异常") #处理全部其它异常
else:
    print("没有异常发生") #没有异常发生
finally:
    print("你们绕不过我，必须执行") #必须执行的代码
    
#异常参数

try:
    x = 1 / 0  # 除数为0
except ZeroDivisionError as err: #为异常指定变量err
    print("Exception")
    print(err.args) #打印异常的参数元组
    print(err) #打印参数，因为定义了__str__()


def diyException(level):
    if level > 0:
        raise Exception("raise exception", level)  #主动抛出一个异常，并且带有参数
        print('我是不会执行的') #这行代码不会执行

try:
    diyException(2)  #执行异常方法
except Exception as err: #捕获异常
    print(err) #打印异常参数

print('-------')
#try:
#   diyException(2)  #执行异常方法
#except 'raise exception' as err: #捕获异常
#    print(err) #打印异常参数

import traceback
try:
   diyException(2)  #执行异常方法
except Exception: #捕获异常
    traceback.print_exc()


#自定义异常
class DiyError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise DiyError("my diy exception") #触发异常
except DiyError as e:
    print(e)


with open("base.py") as f:
    for line in f:
        print(line, end="")
print('\n')
try:
    with open("base1.py") as f:
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print("文件没找到")