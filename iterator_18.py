from typing import Iterable, Iterator


class bothIterAndNext:
    def __iter__(self):
        pass
    def __next__(self):
        pass

class onlyIter:
    def __iter__(self):
        pass

# 迭代器是标准的内置类 需要同时具备__iter__ 和__next__方法
print(isinstance(bothIterAndNext(),Iterable))

print(isinstance(bothIterAndNext(),Iterator))

print(isinstance(onlyIter(),Iterable))

print(isinstance(onlyIter(),Iterator))

li = [1,2,3,4,5,6]
li_iterator=iter(li)
print(isinstance(li,Iterable))
print(isinstance(li,Iterator))
print(isinstance(li_iterator,Iterable))
print(isinstance(li_iterator,Iterator))

print(next(li_iterator))
print(next(li_iterator))
print(id(li_iterator))
li_iterator=iter(li_iterator)
print(next(li_iterator))
print(id(li_iterator))

# 实现自定义迭代器
class Reverse:
    """反向遍历序列对象的迭代器"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.index == 0:
                raise StopIteration #捕获异常
        except StopIteration:#处理异常
            print("迭代器遍历结束")
        else:
            self.index = self.index - 1
            return self.data[self.index]
rev=Reverse(li)
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))