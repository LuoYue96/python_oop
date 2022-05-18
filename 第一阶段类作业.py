#题目
class Person(object):
    __instance = None
    __isinit = True
    school='xxx'
    def __init__(self):
        if Person.__isinit:
            self.__name='auto'
            self.__age=19
            Person.__isinit=False
    def __str__(self):
        return '{}的年龄是{}'.format(self.__name,self.__age)
    @property
    def age(self):
        return self.__age
    @property
    def name(self):
        return self.__name
    @age.setter
    def age(self,age):
        if age < 120 and age > 0:
            self.__age=age
        else:
            print('vaid input')
    @name.setter
    def name(self,name):
        self.__name=name
    def __new__(cls, *args, **kwargs):
        #if not hasattr(cls,'__instance'):
        if not cls.__instance:
            cls.__instance=super().__new__(cls,*args,**kwargs)
        return cls.__instance
lm=Person()
lm.name='ly'
lm.age=100
lm.school='aaa'
print(id(lm))
print(lm)
xiaogou=Person()
print(id(xiaogou))
print(xiaogou)
print(xiaogou.school)
#动态绑定实例方法
import types
def run(self):
    print('这是动态绑定实例方法')
lm.run=types.MethodType(run,lm)
lm.run()
#动态绑定类方法
@classmethod
def getInfo(cls):
    print('这是动态绑定的类方法')
Person.getInfo=getInfo
Person.getInfo()
这是我在个人电脑修改的