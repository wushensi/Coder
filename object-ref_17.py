a = 100000
print(id(a))

a = 100000
print(id(a))

a = 1001
print(id(a))

b = [1,2]
print('b ---',id(b))

b = [1,2]
print('b ---',id(b))

for b in range(300):
    if b is not range(300)[b]:
        print("常量池最大值为：", (b - 1))
        break

c = [1,2,3,4,5]
cc = c
print(id(c))
c[2]=33
print(id(c))

c.append(6)
print(id(c))

print(cc)
print(id(cc))

num=1000
print(id(num))

# 相加再赋值
num +=1
print(id(num))

list1=[1,2,3,4]

#对列表对象和数值对象来说，加法运算的底层实现是完全不同的，在简单的加法中，列表的运算还是创建了一个新的列表对象；但在简写的加法运算+=实现中，则并没有创建新的列表对象。这一点要十分注意。
print(id(list1))

list1+=[5]

print(id(list1))
# 前面（第3天：Python 变量与数据类型[8]）我们提到过，Python 中的六个标准数据类型实际上分为两大类：可变数据和不可变数据。其中，列表、字典和集合均为“可变对象”；而数字、字符串和元组均为“不可变对象”。实际上上面演示的数值数据（即数字）和列表之间的差异正是这两种不同的数据类型导致的
tuple1=(1,2,3)

print(id(tuple1))

print(id(tuple1[1:]))

var1 = 10000
print(var1 == 10000)
#交互执行 结果为False 脚本执行 为True
print(var1 is 10000)
print(id(var1))
print(id(10000))