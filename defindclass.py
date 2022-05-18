"""
类（class）由三部分组成：类名，属性，方法
class 类名：
    属性
    方法
对象：对象是类的实例化，继承了类的所有方法属性
实例方法：在类的内部定义，第一个参数默认是self
类属性：在类的内部定义的变量 【类属性】
实例属性：定义在实例方法里面的变量,形式为 self.变量
__init__ 初始化方法，用于传递参数
    1.是python的内置函数 使用双下划线包起来的【模式方法】
    2.是一个初始化的方法，用来定义实例属性和初始化数据的，在创建对象的时候自动调用
    3.利用传参的机制可以让让我们定义功能更加强大且方便的类
self:只有在类中定义实例方法的时候才有意义，在调用的时候不必传入参数，而是由python解释器自动去指向对象地址
self的名字是可以更改的，可以定义成其他的名字，只是约定俗成的定义成了self
self 指向的是类实例对象本身
"""
# class Human():
# #    name='ABC'      #类属性
#     age=19
#     def __init__(self,name,age,sex):
#         self.name=name                              #实例属性
#         self.age=age
#         self.sex=sex
#         pass
#     def eat(self,food):      #类方法
#         print('eat some food '+food)
#     def run(self):
#         print('run qickly')
#     def __del__(self):
#         print('done')
# ab = Human('apple',18,'male')
# ab.eat('hamber')
# ab.run()
# print(ab.name)
'''
继承：子类继承父类的属性方法，且子类可以有自己的属性和方法
单继承：子类只继承一个父类
多继承：子类继承多个父类
#单继承
'''
'''单继承
# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print('{} eating'.format(self.name))
#     def drink(self):
#         print('{} drinking'.format(self.name))
# 
# class Dog(Animal):      #单继承
#     def wwj(self):
#         print('dog wangwang jiao')
# class Cat(Animal):
#     def mmj(self):
#         print('cat miaomiao jiao')
# print('*'*32)
# dog = Dog('大黄')
# print(dog.name)
# dog.eat()
# dog.drink()
# print('*'*32)
# cat = Cat('小猫')
# print(cat.name)
# cat.eat()
# cat.drink()
'''
#多继承
'''
class A:
    def haha(self):
        print('Ahaha')
class B(A):
    pass
class C(A):
    def haha(self):
        print('Chaha')
class D(C,B):   #多继承，同时继承C和B
    pass
t=D()
t.haha()        #当遇到子类和父类具有相同名称的构造方法时，调用顺序。D->C->B->A （广度优先）
print(D.__mro__)    #可以通过魔法方法__mro__来显示继承调用关系，查询调用顺序
'''
#间接继承
'''父类又称基类，子类为派生类，父类的属性和方法可以一级一级传递，但是通常开发中不超过三级'''
#重写
'''即子类中有一个和父类中相同的名字的方法，子类的同名方法会覆盖掉父类的；super（）可以自动找到父类的帆帆
super.__init__()'''
'''
class Dog():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def jiao(self):
        print('{} 正在旺旺大叫'.format(self.name))
class T(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,color)   #手动调用 父类的方法，执行完毕就继承了name和color这两个实例
        #super.__init__(name,color)      #super自动调用父类 进而调用父类方法，如果有多个父类，会按照广度优先，顺序找到后调用
    def jiao(self):
        print('这是子类对父类方法的重写%s'%(self.name))
'''
#多态
'''
class A(Dog):
    def jiao(self):
        print('这是A在叫')
def commonInvoke(obj):
    obj.jiao()
listcls=[Dog('dahuang','yellow'),A('杜宾','紫色'),T('旺财','蓝色')]
for item in listcls:
    commonInvoke(item)
'''
#类方法和静态方法
# import time
# class Country():
#     name='china'
#     def __init__(self,name):
#         self.name=name
#     @classmethod        #装饰器classmethod 装饰后的方法属于类方法
#     def get_country(cls):
#         return cls.name #访问类属性
#     @staticmethod       #装饰器staticmethod修饰静态方法
#     def get_data():     #静态方法与类属性、实例属性没有交互，不需要传递参数。可以用实例对象来调用，但是一般不会这样做，静态方法直接用类调用，节省内存开支
#         return time.strftime('%H:%M:S',time.localtime())
#
# #print(Country.get_country())    #可以直接访问类方法
# #NV=Country()
# #print('object is : %s'%NV.get_country())
# print(Country.get_data())       #无需传入class的init参数，即可直接调用
# print(time.strftime('%y-%m-%d %H:%M:%S',time.localtime()))
#私有化方法
# class  Person:
#     __action='跳舞'       #私有化类属性
#     def __init__(self):
#         self.__name='李四'    #加两个下划线，将此属性私有化,就不能再外部直接访问了
#         self.age=30
#         pass
#     def __str__(self):
#         return '{}的年龄是{}'.format(self.__name,self.age) #私有化属性可以在类的内部调用
# class Student(Person):
#     def Info(self): #在子类内部调用父类的私有化属性,私有化属性无法被子类继承
#         print(self.__name)
#     pass
# xl=Person()
# #print(xl.__name)      #是通过类对象在外部访问的，无法访问
# #print(Person.__name)    #也无法在类的外部通过类直接访问
# print(xl)
# print(xl.__action)  #私有化类属性无法被类对象访问
# stu=Student()
# print(stu.__name)   #子类也无法调用父类的私有化属性
#私有化属性
'''
# class Person:
#     def __init__(self):
#         self.__age = 18     #私有化属性
#     def getage(self):
#         return self.__age
#     def setage(self,age):
#         if age < 0:
#             print('年龄不能小于0')
#         else:
#             self.__age=age
#     #方法1，通过property实现直接访问私有化属性
#     #定义一个类属性，实现通过直接访问属性的形式去访问私有化属性的值
#     age=property(getage,setage)
# p1 = Person()
# print(p1.age)   #可以直接访问私有化属性age
# p1.age=22       #可以直接修改私有化属性age
# print(p1.age)
# class Person2(object):
#     def __init__(self):
#         self.__age=18
#     #实现方式2 ，通过装饰器实现直接在外部访问私有化属性
#     @property       #用装饰器修饰，添加属性标识，提供一个getter方法
#     def  age(self):
#         return self.__age
#     @age.setter     #用装饰器修饰，添加一个setter方法
#     def  age(self,parms):
#         if parms <0:
#             print('年龄不能小于0')
#         else:
#             self.__age=parms
# p1 = Person2()
# print(p1.age)   #可以直接访问私有化属性age
# p1.age=-1       #可以直接修改私有化属性age
# print(p1.age)
'''
