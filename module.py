# 0x1 模块(module)其实就是 py 文件，里面定义了一些函数、类、变量等
# 0x2 包(package)是多个模块的聚合体形成的文件夹，里面可以是多个 py 文件，也可以嵌套文件夹
# 0x3 库是参考其他编程语言的说法，是指完成一定功能的代码集合，在 Python 中的形式就是模块和包

# 简单导入
#import subModule

# 使用 from/import 导入，可以省略模块名称 直接调用
#from subModule import subFun1

# 通用导入 使用通配符*
from subModule import *

# 调用包 中的模块方法
from pkg import mod1

def callModule():
    print("this is python module")

# 演示一个模块调用
#subModule.subModule()

subFun2()

mod1.callFun1()


