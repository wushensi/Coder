#类的内置方法
#方法	说明
#__init__	构造函数，在生成对象时调用
#__del__	析构函数，释放对象时使用
#__repr__	打印，转换
#__setitem__	按照索引赋值
#__getitem__	按照索引获取值
#__len__	获得长度
#__cmp__	比较运算
#__call__	函数调用
#__add__	加运算
#__sub__	减运算
#__mul__	乘运算
#__div__	除运算
#__mod__	求余运算
#__pow__	乘方

# 类的定义
class Car:
    #类方法
    #name = 'Chinese multifunction car'
    def __init__(self,name):
        self.name=name   

    def drive(cls,speed):
        print(cls.name,'drive operation','speed is', speed)
    
    @classmethod
    def GuessCharge(self):
        print('charge guess')
    
    @staticmethod
    def clearCar():
        print('clear car')

# 对象实例化
c = Car('BMW')

#c.drive()
c.drive(100)

# 第二种方式 静态方法
#Car.drive(110) driver 需要@classmethod 修饰 就可以类直接调用 普通方法默认带一个参数 可以用self来指代
Car.GuessCharge()

#静态方法（可调类变量、可被实例调用、可被类调用）
#1、用 @staticmethod 装饰的不带 self 参数的方法；
#2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
#3、调用时并不需要传递类或实例。
Car.clearCar()

# 类的继承
class RaceCar(Car):
    def description(self):
        print(self.name,"this is a race car")

rc = RaceCar("V")
rc.description()
# 调用父类方法
rc.clearCar()
rc.drive(100)

#类的多态
class Bus(Car):
    def drive(cls,speed):
        print(cls.name,'drive operation','speed is', speed)
    
class PoilceVehicle(Car):
    def drive(cls,speed):
        print(cls.name,'drive operation','speed is', speed)
    
bus=Bus("Bus")
pv=PoilceVehicle("PoliceVehicle")

#父类
c.drive(100)

#子类1 继承父类 复写了drive方法
bus.drive(80)

#子类2 继承父类 复写了drive方法
pv.drive(110)