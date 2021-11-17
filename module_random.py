import random
print(random.random())

#生成5-50之间的随机数
print(random.randint(5,50))

#生成2-5直接的浮点数
print(random.uniform(5,2))

'''
sample(sequence, k)函数可以获取从总体序列或集合中选择的唯一元素的k长度列表。
sample()函数不会修改原有序列，它主要用在无重复的随机抽样场景，实现从大量样本中快速进行抽样。例如：
'''
lst = [1,2,3,4,5]  
print(random.sample(lst,4))  
print(lst)

print(random.randrange(2,5))
#生成1-10直接的随机数，步长为2 
print(random.randrange(1,10,2))

#在有序列表中随机返回一个，可以是列表 元组
strlist = ['C++','C#','Java','Python']  
strtemp = ('Do you love python')  
print(random.choice(strlist))
print(random.choice(strtemp))

#把有序列表中的顺序打乱，重新输出
lst = ['A' , 'B', 'C', 'D', 'E' ]
random.shuffle(lst)  
print (lst)