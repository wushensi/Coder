
from collections import namedtuple
User = namedtuple("User",["name", "age", "weight"])
user = User("admin", "20", "60")
name, age, weight = user
print(user[0])
print(name, age, weight)
print(user.name, user.age, user.weight)
print(type(User))

# 将序列直接转换为新的 tuple 对象
user1 = ["root",32,60]
user1 = User._make(user1)
print(user1)

# 返回一个 dict
user = User("admin", 20, 60)
print(user._asdict()) 

from collections import ChainMap

user1 = {"name":"admin", "age":"20"}
user2 = {"name":"root", "weight": 65}
users = ChainMap(user1, user2)
print(users.maps)

users.maps[0]["name"] = "tiger"
print(users.maps)
print(user1)

for key, value in users.items():
    print(key, value)

from collections import deque
q = deque([1, 2, 3])
q.append('4')
q.appendleft('0')
print(q)
q.popleft()
q.pop()
print(q)

from collections import Counter

animals = ["cat", "dog", "cat", "bird", "horse", "tiger", "horse", "cat"]
animals_counter = Counter(animals)
print(animals_counter)
print(animals_counter.most_common(1))
print(animals_counter)


from collections import OrderedDict

user = OrderedDict()
user["name"] = "admin"
user["age"] = 23
user["weight"] = 65
print(user)
user.move_to_end("name") # 将元素移动至末尾
print(user)
user.move_to_end("name", last = False) # 将元素移动至开头
print(user)
print(user.keys())
print(type(user.values()))

'''
defaultdict 是内置 dict 类的子类。它实现了当 key 不存在是返回默认值的功能，
除此之外，与内置 dict 功能完全一样。
'''
from collections import defaultdict

default_dict = defaultdict(int)
default_dict["x"] = 10
print(default_dict["x"])
print(default_dict["y"])
print(default_dict["z"])


def getUserInfo():
    return {
        "name" : "",
        "age" : 0
    }
#print(type(getUserInfo()))

default_dict = defaultdict(getUserInfo)
admin = default_dict["admin"]
print(admin)
admin["age"] = 34
print(admin)

# 输出如下
{'name': '', 'age': 0}
{'name': '', 'age': 34}