'''
enum 是一组绑定到唯一常数值的符号名称，并且具备可迭代性和可比较性的特性。我们可以使用 enum 创建具有良好定义的标识符，
而不是直接使用魔法字符串或整数，也便于开发工程师的代码维护。

属性是不可以重复的，内容是可以重复
'''

from enum import Enum,auto,unique,IntEnum

class HttpStatus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = auto.value

print("HttpStatus enum name {}",HttpStatus.BAD_REQUEST) #enum
print("HttpStatus enum name {}",HttpStatus.BAD_REQUEST.name) #basic value
print("HttpStatus enum value {}",HttpStatus.BAD_REQUEST.value) #basic value
print(isinstance(HttpStatus.OK, HttpStatus))            # True

for status in HttpStatus:
    print('{} : {}'.format(status.name, status.value))


#for name, member in HttpStatus.__members__.items():
#    print('{} : {}'.format(name, member))

#通过value访问
print(HttpStatus(200))

#通过name访问
print(HttpStatus['SERVICE_UNAVAILABLE'])

'''
上面我们创建的枚举类中，value 值是可以重复的，如果我们不想枚举类中的值重复可以是用装饰器 @unique
'''

'''
ValueError: duplicate values found in <enum 'HttpStatusPlus'>: SERVICE_UNAVAILABLE -> OK
'''
@unique
class HttpStatusPlus(Enum):
    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    SERVICE_UNAVAILABLE = 500
    OTHER = auto.value

print(HttpStatusPlus.BAD_REQUEST)

print('---')

import unittest
#class TestEnum1(unittest.TestCase):
#    def test_auto_number(self):
#        class Color(Enum):
#            red = auto()
#            blue = auto()
#            green = auto()
#        self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
#        self.assertEqual(Color.red.value, 1)
#        self.assertEqual(Color.blue.value, 2)
#        self.assertEqual(Color.green.value, 3)
#    
#    def test_auto_name(self):
#        class Color(Enum):
#            def _generate_next_value_(self, start, count, last):
#                return self
#            red = auto()
#            blue = auto()
#            green = auto()
#        self.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
#        self.assertEqual(Color.red.value, 'red')
#        self.assertEqual(Color.blue.value, 'blue')
#        self.assertEqual(Color.green.value, 'green')
#unittest.main()


#枚举对象的值比较

class TestEnum2(unittest.TestCase):
    class Season(IntEnum):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4

    def test_comparisons(self):
        season = self.Season
        self.assertEqual(season.SPRING, 1)
        class Part(Enum):
            SPRING = 1
            CLIP = 2
            BARREL = 3
        self.assertNotEqual(Part.SPRING, 1)
        self.assertNotEqual(Part.SPRING, season.SPRING)

#unittest.main()

class Mood(Enum):
    FUNKY = (1, "hello")
    HAPPY = (3, "world")

    def describe(self):
        return self.name, self.value

    def __init__(self, num, nice):
        self.num = num
        self.nice = nice

    def __str__(self):
        return 'my custom str! {0}'.format(self.value)

    @classmethod
    def favorite_mood(cls):
        return cls.HAPPY

    @property
    def testValue(self):
        return self.nice + ':' + str(self.num)

print(Mood.favorite_mood()) 
print(Mood.HAPPY.describe())
print(str(Mood.FUNKY))      
print(Mood.FUNKY.testValue) 

print("---")

class EnumExtend(unittest.TestCase):
    def test_extending(self):
        class Shade(Enum):
            def shade(self):
                print(self.name)

        class Color(Shade):
            red = 1
            green = 2
            blue = 3
        with self.assertRaises(TypeError):
            class MoreColor(Color):
                cyan = 4
                magenta = 5
                yellow = 6

    def test_extending2(self):
        class Shade(Enum):
            def shade(self):
                return self.name

        class Color(Shade):
            def hex(self):
                return '%s nice!' % self.value

        class MoreColor(Color):
            cyan = 4
            magenta1 = 5
            yellow = 6
        self.assertEqual(MoreColor.magenta1.shade(), 'magenta1')
        self.assertEqual(MoreColor.magenta1.hex(), '5 nice!')

unittest.main()