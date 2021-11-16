import sys
print("The list of command line arguments:\n",sys.argv)

print(sys.executable)

#返回一个字典,包含系统已经加载的模块名称
print(sys.modules)

#系统内置模块名称
print(sys.builtin_module_names)

#该属性是一个由字符串组成的列表，其中各个元素表示的是 Python 搜索模块的路径；在程序启动期间被初始化
print(sys.path)

#标准输入
#print(sys.stdin.readline())


#文件读取
#try:
#    f = open('basic IO.py', 'r',encoding='UTF-8')
#    sys.stdin=f
#    print(sys.stdin.read())
#finally:
#    if f:
#        f.close()

#标准输出流与文件流绑定，作为日志功能 记录
#sys.stdout = open('d:\\test1.txt','w',encoding='UTF-8')
#sys.stderr = open('d:\\test2.txt','w',encoding='UTF-8')

print('''
#文件读取
#try:
#    f = open('basic IO.py', 'r',encoding='UTF-8')
#    sys.stdin=f
#    print(sys.stdin.read())
#finally:
#    if f:
#        f.close()
''')
print('''
#文件读取
#try:
#    f = open('basic IO.py', 'r',encoding='UTF-8')
#    sys.stdin=f
#    print(sys.stdin.read())
#finally:
#    if f:
#        f.close()
''')
print('''
#文件读取
#try:
#    f = open('basic IO.py', 'r',encoding='UTF-8')
#    sys.stdin=f
#    print(sys.stdin.read())
#finally:
#    if f:
#        f.close()
''')

#构造stderr标准错误输出
#a=1/0

#获取递归大小
print(sys.getrecursionlimit())

#获取数据内存空间占用
print(sys.getsizeof(2**30-1))

print(sys.int_info)
print(sys.float_info)