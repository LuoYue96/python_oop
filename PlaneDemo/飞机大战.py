'''
飞机大战需求描述：
    1.存在四个对象:我方飞机、敌方飞机、我方子弹、敌方子弹
    2.功能：
        a.背景音乐
        b.我方飞机可以移动（根据按键控制） 敌方飞机也可以移动（随机的自动移动）
        c.双方飞机都可以发送子弹
步骤：
1.创建一个窗口
2.创建一个我方飞机，根据方向键左右的移动
3.给我方飞机添加发射子弹的功能（按下空格键去发送）
4.创建一个敌人飞机
5.敌人飞机可以自由的移动
6.敌人飞机可以自动的发射子弹

在安装pygame模块的时候尤其要注意一下
如果在pycharm中安装不成功 提示：”EOFEOOR：EOF when reading a line“ ，原因是pycharm与该库存在不兼容，属于pycharm的bug
此时可以采用另一种安装方式：

'''
#以下为面向过程编程
import pygame.image

'''
#coding =utf-8
import pygame
from pygame.locals import *
def main():
    #首先创建一个窗口，用来显示内容
    screen=pygame.display.set_mode((600,800),1,35)
    #创建一个背景图片对象
    background=pygame.image.load('./picture/1.jpg')
    #设置一个title
    pygame.display.set_caption('飞机大战')
    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./picture/background.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1) #循环次数，-1表示无限循环
    #载入玩家的飞机图片
    hero=pygame.image.load('./picture/hero.png')
    #初始化位置
    x,y=0,0
    #设定要显示的内容
    while True:
        screen.blit(background,(0,0))
        #显示玩家飞机的图片
        screen.blit(hero,(x,y))
        #获取键盘事件
        eventlist=pygame.event.get()
        for event in eventlist:
            if event.type==QUIT:
                print('退出')
                exit()
            elif event.type==KEYDOWN:
                if event.type==K_a or event.key==K_LEFT:
                    print('left')
                    if x>0:
                        x-=10
                elif event.type==K_d or event.key==K_RIGHT:
                    print('right')
                    if x<430:
                        x+=10
                elif event.key==K_SPACE:
                    print('K_SPACE')
        #更新显示内容
        pygame.display.update()
    pass
if __name__ == '__main__':
    main()
'''
#以下为面向对象编程
'''
1.实现飞机的显示，并且可以控制飞机的移动【面向对象】
'''
import pygame
from pygame.locals import *
class HeroPlane(object):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen:主窗体对象
        '''
        #飞机的默认位置
        self.x=150
        self.y=750
        #设置要显示的内容的窗口
        self.screen=screen
        #生产飞机的图片对象
        self.imageName='./picture/hero.png'
        self.image=pygame.image.load(self.imageName)
        pass
    def movelift(self):
        '''左移动'''
        if self.x > 0:
            self.x-=10
        pass
    def moveright(self):
        '''右移动'''
        if self.x <600:
            self.x+=10
        pass
    def moverDown(self):
        ''''下移动'''
        if self.y > 0:
            self.y-=10
        pass
    def moverUp(self):
        ''''上移动'''
        if self.y <750:
            self.y+=10
        pass
    def display(self):
        '''
        在主窗口中显示飞机
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        pass
def keyboard_control(Planobj):
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == QUIT:
            print('退出')
            exit()
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                Planobj.movelift()
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                Planobj.moveright()
            elif event.type == K_w or event.key == K_UP:
                print('up')
                Planobj.moverUp()
            elif event.type == K_s or event.key == K_DOWN:
                print('down')
                Planobj.moverDown()
            elif event.key == K_SPACE:
                print('射了一发子弹')
def main():
    # 首先创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((600, 800), 1, 35)
    # 创建一个背景图片对象
    background = pygame.image.load('./picture/1.jpg')
    # 设置一个title
    pygame.display.set_caption('飞机大战')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./picture/background.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  # 循环次数，-1表示无限循环
    # 创建一个飞机对象
    hero=HeroPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        hero.display()
        # 获取键盘事件
        keyboard_control(hero)
        # 更新显示内容
        pygame.display.update()
        pass
if __name__ == '__main__':
    main()
