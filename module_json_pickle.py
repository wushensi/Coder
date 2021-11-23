#字典转成json字符串 加上ensure_ascii=False以后，可以识别中文， indent=4是间隔4个空格显示

import json         
d={'小明':{'sex':'男','addr':'上海','age':26},'小红':{ 'sex':'女','addr':'上海', 'age':24}}
print(json.dumps(d,ensure_ascii=False,indent=4))
#字典转成json字符串,不需要写文件，自动转成的json字符串写入到‘users.json’的文件中 
                                                                       
#d={'小明':{'sex':'男','addr':'上海','age':26},'小红':{ 'sex':'女','addr':'上海', 'age':24},}
##打开一个名字为‘users.json’的空文件
#fw =open('users.json','w',encoding='utf-8')
#json.dump(d,fw,ensure_ascii=False,indent=4)

#fw.close()

#!/usr/bin/python3
#把json串变成python的数据类型   
#import json  
#打开‘users.json’的json文件
f =open('users.json','r',encoding='utf-8')
#读文件
res=f.read()
print(json.loads(res))
print(type(json.loads(res)))
f.close()
#load 从文件读取，不需要先读取文件内容
f =open('users.json','r',encoding='utf-8')
print(json.load(f))

print('***pickle***')

# dumps功能 
import pickle
data = ['A', 'B', 'C','D']  
datastr = pickle.dumps(data)
print(pickle.dumps(data))

# dump功能
with open('pickle.txt', 'wb') as f:
    pickle.dump(data, f) #二进制存储
print('写入成功')

# loads功能
msg = pickle.loads(datastr) #反序列化
print(msg)

# load功能
with open('pickle.txt', 'rb') as f:
   data = pickle.load(f)
print(data)