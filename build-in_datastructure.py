# Python 内置数据结构 字符串、列表、元组 集合 字典

# 字符串 创建
str_ds1='this is string ds1'

str_ds2="this is string ds2"

str_ds3='''
description for author
description for version
description for date
'''

print(str_ds1)

print(str_ds2)

print(str_ds3)

# 列表创建
## var v1= list() or v1=[] 创建列表
list1=[1,2,3]
list2=[1,"e",3.01]
#print(list1)

b = list('abc')

c=list((1,2,3))

d=list({"a":1,"b":3})

e=list(range(100))

print(e)

## 用列表推导式创建列表
f = [i for i in range(5)]
#遍历
#for item in list1:
#    print(item)
#
#for item in list2:
#    print(item)
#
#for item in b:
#    print(item)

print(c)

print(d)



for item in c:
    print(item)

for item in d:
    print(item)

#for item in e:
#    print(item)

print(range(10))

print(f)

# 创建字典的5种方式
d1={'a':1,'b':2,'c':3}

d2={'a':'a','b':18,'c':['teacher',0,{'a':1,'b':'c'}]}

d3=dict(name='a',age=19)

d4=dict([('software','Coder'),('version','v2.0')])

print(d2)

print(d3)

print(d4)

## 使用zip函数创建字典
x = ['name','age','job']
y = ['a',10,'c']

d5 = dict(zip(x,y))
print(d5)

### 创建空字典
f = {}
print(f)

g= dict()
print(g)

d6 = dict.fromkeys(['name','age','a'])
print(d6)