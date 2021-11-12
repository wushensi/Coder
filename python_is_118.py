'''
Python 中一切皆是对象，对象包含 id（唯一身份标识），type（类型） 和 value（值） 三个要素。id 可以通过函数 id(obj) 来获取。
因此 is 操作符就相当于比较两个对象的 id 是否相同，而 == 操作符则相当于比较两个对象的 value 是否相同。
'''

a = 1000
b = 1000
print( a == b) #值的比较
print( a is b) #对象的比较 

a = [1, 'hello', [1,2]]
b = list(a)
a[0] = 100
a[2][0] = 100
print(a)
print(b)
print(id(a))
print(id(b))
print(id(a[2]))
print(id(b[2]))

#通过切片来实现浅拷贝
a = [1, 2, 3]
b = a[:]
print(a == b)
print(a is b)

#对于顶层不可变的对象，不存在对象的拷贝，因为都是指向同一个对象，没有新的对象产生。
a = (1,2,3)
b = tuple(a)
print(a == b)
print(a is b)

import copy
#深拷贝递归拷贝顶层对象以及它内部的子对象，因此，新对象和原来的旧对象，没有任何关联
a = [1, 'hello', [1,2]]
b = copy.deepcopy(a)

a[0] = 100
a[2][0] = 100
print(a)
print(b)

a = (1,2,[1,2])
b = copy.deepcopy(a)
print(a is b)
print(id(a[2]))
print(id(b[2]))
a[2][1]=1
print(a)
print(b)