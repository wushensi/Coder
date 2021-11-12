def sayHello(name): # name 是形式参数
    print("Hello %s" % name)
#函数主体
name = "hanmeimei" # name 是实际参数
#函数调用
sayHello(name)

#交换 打印输出形参
def swap(a, b):
    a, b = b, a
    print("in swap a = %d and b = %d " % (a, b))

# 值传递，实参和形参互补干扰，变量都是指向一个地址，基础数据类型 值传递
a = 100
b = 200
swap(a, b)
print("in main a = %d and b = %d " % (a, b))

# list 对象，引用传递
def swap(list):
    list.append(4)
    print("in swap list is %s " % list)

def swap1(list):
    list=list+[4] #会生成一个新对象，与原来的引用变量互补影响
    print("in swap list is %s " % list)

def swap2(list):
    list=list+[4] #会生成一个新对象，与原来的引用变量互补影响
    print("in swap list is %s " % list)
    return list #返回最新对象的地址
list_x = [1, 2, 3]
#swap(list_x)
swap1(list_x)
print("in main list is %s " % list_x)
list_x=swap2(list_x)
print("in main list is %s " % list_x)