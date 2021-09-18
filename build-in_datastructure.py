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

print(str_ds1[-5])

str_slide=['https://www.cnblogs.com/index.html']

str_slide1=[1,2,3,4,5,6,7,8,9,10]

print(str_slide[0][0:8])
print(str_slide[0][:8])

print(str_slide1[:1])
print(str_slide1[:8])
#另外需要注意的是负数步长是从元素尾部到前遍历整个序列，所以负数的分片开始索引一定要大于结束索引
print(str_slide1[-10:])
print(str_slide1[-8:])

print(str_slide1[::-1])
print(str_slide1[:0:-1])
print(str_slide1[:1:-1])
print(str_slide1[:2:-1])
print(str_slide1[:3:-1])
print(str_slide1[:4:-1])
print(str_slide1[:5:-1])
#列表可以相乘
print(str_slide1*3)

print(len(str_slide1*3))
list1=[1,2,'3']
list2=[4,5,6]

#list的append方法
str_slide1.append(list1)

print(str_slide1)

#count方法统计频次
print(str_slide1.count(1))

str_slide1.extend(list2)

print(str_slide1)

str_slide1.insert(1,2)

print(str_slide1.reverse())

#其他相关操作 pop\remove\reverse\sort

num=[100,2,3,4,5,6,7,8,1000]

print(num.reverse())

num.clear()

print(num)

fruits=['apple','b','c']

fruits.reverse()

print(fruits)

## 元组的基本操作 元组三种定义方式
tup1=('a',2,3,4,5)
tup2=(1,2,3,4,5)
tup3='a','b',1,2,3

print(type(tup1))
print(type(tup2))
print(type(tup3))

## 可以对元组进行分片操作
print(tup1[0])
print(tup1[:3])

# 元组创建后，元素不能删除，可以通过del 删除整个元组
# 列表使用[] 方括号，元组使用小括号()
del tup1
#print(tup1)
print(tup2+tup3*3)

#元组中元素判断
print( 'a' in tup2)

print(tup2[0])
print(tup2[1])
print(tup2[-1])

# 列表转换未元组，同时元组可以专为列表
l1=[1,2,3,4,5,6,7,8,9,0]
t1=tuple(l1)
print(t1)
print(type(t1))
l2=list(t1)
print(l2)
print(type(l2))


## 字典基础操作, 键唯一 ，覆盖 最新为准

dic1 = {'name':'zhangsan','age':23,'address':'BeiJing','name':'lisi'}
print(dic1)

#dic1.clear()

# 字典复制 类似深度复制 完整复制，底层重新创建 id不同
dic2=dic1.copy()

# 类似浅拷贝,dic1的内容变化，dic3也会跟着变 id相同
dic3=dic1

print(id(dic1))
print(type(dic1))
#del dic1
dic1['name']='abc'
print(dic2)
print(dic3)
print(id(dic2))
print(id(dic3))

tuple1=('name','age','score')

print(dict.fromkeys(tuple1,(1,2,3)))

#key in dict 字典中查询键
print('name' in dic1)

l3=list(dict.items(dic1))
#字典以列表方式返回元组数组
print(l3)

#keys() 返回一个迭代器
l4=dic1.keys()
print(type(l4))
for item in l4:
    print(item)



