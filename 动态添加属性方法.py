#动态添加属性
'''
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)
ly=Student('罗越',26)
print(ly)
#---------通过实例动态添加属性，属性归实例所有--------
ly.weight=140
print(ly.weight)
xm=Student('小明',18)
#print(xm.weight)  #其他实例对象无该属性
#---------通过类添加属性-------------
Student.school='河北地质大学'
print(ly.school)
print(xm.school)    #类动态添加的属性属于类，所有实例化对象均继承该属性
'''
#动态添加方法
#动态添加实例方法，需要使用types（import types）
 