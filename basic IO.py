#括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换
print('{}website:{}!'.format('python tech','www.python.com'))

print('{0} 和{1}'.format('This is ','Python'))

#在括号中的数字用于指向传入对象在 format() 中的位置
print('{1} 和{0}'.format('This is ','Python'))

#如果在 format() 中使用了关键字参数，那么它们的值会指向使用该名字的参数
print('{name} website:{site}'.format(name='Python tech',site='http://www.python.org'))

#位置及关键字参数可以任意的结合
print('{site} website:{site},name:{name}, person is {0}, age is {1}'.format('Tom',15,name='Python tech',site='http://www.python.org'))

# 已repr() 输出 或者 以 str输出
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
print("repr() shows quotes: {!a}; str() doesn't: {!s}".format('test1', 'test2'))

# 保留三位小数
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}

#在字段后的 : 后面加一个整数会限定该字段的最小宽度
print(type(table.items()))
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))
    print('{0:30} ==> {1:20d}'.format(name,phone))

#如果有个很长的格式化字符串，不想分割它可以传入一个字典，用中括号( [] )访问它的键；
table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789789789789}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#要读取文件内容，调用 read(size) ，size为可选参数
f=open('base.py','r')
str=f.read(50)
print(str)
f.close()

#读取一行，换行符为 \n
f=open('base.py','r')
str_line=f.readline()
print(str_line)
f.close()

#读取文件中包含的所有行，可设置可选参数 size 。
f=open('base.py','r')
str_lines=f.readlines()
#for items in str_lines:
#    print(items)
print(type(str_lines))
f.close()

#覆盖写入
f=open('D:\\0927\\tmp.txt','w')
f.write('this is python')
f.close()

#seek(offset, from_what) 改变文件当前的位置。offset 移动距离；from_what 起始位置，0 表示开头，1 表示当前位置，2 表示结尾，默认值为 0 ，即开头。
f=open('D:\\0927\\tmp.txt','rb+')
f.write(b'0123456789abcdef')
f.seek(10)
print(f.read())
f.close()

f=open('D:\\0927\\tmp.txt','r')
f.seek(5)
print(f.tell())
f.close()

#json序列化 与反序列化
import json
data = {'id':'1', 'name':'jhon', 'age':12}
with open('D:\\0927\\t.json','w') as f:
    json.dump(data,f)

with open('D:\\0927\\t.json','r') as f:
    d=json.load(f)
    print(d)