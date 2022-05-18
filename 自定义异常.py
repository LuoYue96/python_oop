#自定义异常，都是直接或间接继承Error或Exception类；由开发者主动抛出自定义异常，在python中使用raise关键字
#step1编写一个异常类
class ToolongException(Exception):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '你输入的%s超过了五个字符长度！！！'%self.name
    pass
def A():
    name=input('请输入你的名字：')
    if len(name) > 5 :
        raise ToolongException(len(name))
    else:
        print(name)
#A()                 #直接调用会提示异常，异常名字为上面异常类的名字
try:
    A()
except ToolongException as msg :
    print(msg)
else:
    print('异常没有出现，通过')
finally:
    print('不管异常是否捕获到，都执行finally的代码块')