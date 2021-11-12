import os
import psutil

# 打印当前程序占用的内存大小
def print_memory_info(name):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    MB = 1024 * 1024
    memory = info.uss / MB
    print('%s used %d MB' % (name, memory))

# 测试函数
def foo():
    print_memory_info("foo start")
    length = 10000 * 1000
    list = [i for i in range(length)]
    print_memory_info("foo end")

def foo1():
    print_memory_info("foo start")
    length = 1000 * 1000
    list = [i for i in range(length)]
    print_memory_info("foo end")
    return list

def foo2(): #这是因为对于 list_a 和 list_b 来说虽然没有被任何外部对象引用，但因为二者之间交叉引用，以至于每个对象的引用计数都不为零，这也就造成了其所占用的空间永远不会被回收的尴尬局面。这个缺点是致命的。
    print_memory_info("foo start")
    length = 1000 * 1000
    list_a = [i for i in range(length)]
    list_b = [i for i in range(length)]
    list_a.append(list_b)
    list_b.append(list_a)
    print_memory_info("foo end")
    return list

#foo()
#list1=foo1() #  list 变量是局部变量，其作用域是当前函数内部，一旦函数执行完毕，局部变量的引用会被自动销毁 因为被引用，所以内存空间未释放
foo2()
print_memory_info("main end") 