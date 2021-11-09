import datetime
#当前时间
print(datetime.datetime.now())

#指定时间
datetest = datetime.datetime(2021,1,1,1,1,1)
print(datetest)
print(type(datetest))

#取时分秒
print(str(datetest.year)+' - '+str(datetest.month)+' - '+str(datetest.day)+' '+str(datetest.hour)+':'+str(datetest.minute)+':'+str(datetest.second))

#时间戳转换为datetime对象
import time
dt1= datetime.datetime.fromtimestamp(100)
dt2= datetime.datetime.fromtimestamp(time.time())
print(dt1)
print(dt2)

#字符串和日期互转
#字符串-日期
datestr = datetime.datetime.strptime('2019-9-30 22:00:00','%Y-%m-%d %H:%M:%S')
print(datestr)
now = datetime.datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(type(now.strftime('%a, %b %d %H:%M')))

#日期增量表示
now = datetime.datetime.now()
print(now)

newdate = now+datetime.timedelta(hours=10)
print(newdate)

newdate = now-datetime.timedelta(days=1)
print(newdate)

#计算效率
def caclTime():
    item = 1
    for i in range(1,100000):
        item +=i
    return item
startTime = time.time()
result = caclTime()
endTime = time.time()
print('result--->'+str(result))
print('time cost--->'+str(endTime-startTime))

#休眠
for i in range(2):
    print('one')
    print(time.time())
    time.sleep(1)
    print('two')
    print(time.time())
    time.sleep(1)
    print('completed')