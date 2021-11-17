import queue

#FIFO 先入先出示例
#q = queue.Queue()  # 创建 Queue 队列
#for i in range(3):
#    q.put(i)  # 在队列中依次插入0、1、2元素
#for i in range(3):
#    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为0、1、2
#
#LIFO 后入先出示例
#q1=queue.LifoQueue() 
#for i in range(5):
#    q1.put(i)
#
#for i in range(5):
#    print(q1.get())


#q = queue.PriorityQueue()  # 创建 PriorityQueue 队列
#data1 = (1, 'python')
#data2 = (2, '-')
#data3 = (3, '100')
#style = (data2, data3, data1)
#
#print(type(style))
#
#for i in style:
#    q.put(i)  # 在队列中依次插入元素 data2、data3、data1
#for i in range(3):
#    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为 data1、data2、data3
# 
q = queue.SimpleQueue()  # 创建 SimpleQueue 队列

for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为0、1、2

#print(q.get(block=True,timeout=3))
try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100') # 在队列中插入字符串 '100'
    for i in range(4):  # 从队列中取数据，取出次数为4次，引发 queue.Empty 异常
        print(q.get(block=False))
except queue.Empty:
    print('queue.Empty')

try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100') # 在队列中插入字符串 '100'
    q.put('stay hungry, stay foolish', block=False)  # 队列已满，继续往队列中放入数据，引发 queue.Full 异常
except queue.Full:
    print('queue.Full')

# 四种队列的通用方法
q = queue.Queue()
q.put('python-100')  # 在队列中插入元素 'python-100'
print(q.qsize())  # 输出队列中元素个数为1

q = queue.Queue()
print(q.empty())  # 对列为空，返回 True
q.put('python-100')  # 在队列中插入元素 'python-100'
print(q.empty())  # 对列不为空，返回 False

q = queue.Queue(3)  # 定义一个长度为3的队列
print(q.full())  # 元素个数未达到上限，返回 False
q.put('python')  # 在队列中插入字符串 'python'
q.put('-') # 在队列中插入字符串 '-'
q.put('100') # 在队列中插入字符串 '100'
print(q.full())  # 元素个数达到上限，返回 True

'''
item，放入队列中的数据元素。

block，当队列中元素个数达到上限继续往里放数据时：如果 block=False，直接引发 queue.Full 异常；如果 block=True，且 timeout=None，
则一直等待直到有数据出队列后可以放入数据；如果 block=True，且 timeout=N，N 为某一正整数时，则等待 N 秒，如果队列中还没有位置放入数据就引发 queue.Full 异常。

timeout，设置超时时间。
'''

try:
    q = queue.Queue(2)  # 设置队列上限为2
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100', block = True, timeout = 1) # 队列已满，继续在队列中插入字符串 '100'，等待5秒后会引发 queue.Full 异常
except queue.Full:
    print('queue.Full')

'''
相当于 Queue.put(item, block=False)，当队列中元素个数达到上限继续往里放数据时直接引发 queue.Full 异常。
'''
try:
    q = queue.Queue(2)  # 设置队列上限为2
    q.put_nowait('python')  # 在队列中插入字符串 'python'
    q.put_nowait('-') # 在队列中插入字符串 '-'
    q.put_nowait('100') # 队列已满，继续在队列中插入字符串 '100'，直接引发 queue.Full 异常
except queue.Full:
    print('queue.Full')

try:
    q = queue.Queue()
    q.get(block = True, timeout = 1) # 队列为空，往队列中取数据时，等待5秒后会引发 queue.Empty 异常
except queue.Empty:
    print('queue.Empty')

try:
    q = queue.Queue()
    q.get_nowait() # 队列为空，往队列中取数据时直接引发 queue.Empty 异常
except queue.Empty:
    print('q.get_nowait queue.Empty')

q = queue.Queue()
q.put('python')
q.put('-')
q.put('100')
for i in range(3):
    print(q.get())
    q.task_done()  # 如果不执行 task_done，join 会一直处于阻塞状态，等待 task_done 告知它数据的处理已经完成
q.join()
q.put('python')
q.put('-')
q.put('100')

import random
import threading
import time

#生产者线程
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue
    def run(self):
        for i in range(5):
            print ("%s: %s is producing %d to the queue!" %(time.ctime(), self.getName(), i))
            self.data.put(i)  # 将生产的数据放入队列
            time.sleep(random.randrange(10)/5)
        print ("%s: %s finished!" %(time.ctime(), self.getName()))

#消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data=queue
    def run(self):
        for i in range(5):
            val = self.data.get()  # 拿出已经生产好的数据
            print ("%s: %s is consuming. %d in the queue is consumed!" %(time.ctime(), self.getName(), val))
            time.sleep(random.randrange(5))
            self.data.task_done() # 告诉队列有关这个数据的任务已经处理完成
        print ("%s: %s finished!" %(time.ctime(), self.getName()))

#主线程
def main():
    queue1 = queue.Queue()
    producer = Producer('Pro.', queue1)
    consumer = Consumer('Con.', queue1)
    producer.start()
    consumer.start()
    queue1.join()  # 阻塞，直到生产者生产的数据全都被消费掉
    producer.join() # 等待生产者线程结束
    consumer.join() # 等待消费者线程结束
    print ('All threads terminate!')
 
if __name__ == '__main__':
    main()

print(__name__)