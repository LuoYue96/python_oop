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
import random
import time
#创建一个飞机的基类，我方和敌方的飞机可以继承
class BasePlane(object):
    def __init__(self,screen,imagepath):
        '''

        :param screen:主窗体
        :param imagepath: 飞机图片
        '''
        self.screen=screen
        self.image=pygame.image.load(imagepath)
        self.bulletList=[] #存放子弹列表
        pass
    def display(self):
        '''
                在主窗口中显示飞机
                :return:
                '''
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItem = []
        for item in self.bulletList:
            if item.judge():
                needDelItem.append(item)
        # 重新遍历
        for i in needDelItem:
            self.bulletList.remove(i)
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹
            bullet.move()  # 改变子弹的位置
        pass

class HeroPlane(BasePlane):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen:主窗体对象
        '''
        #飞机的默认位置
        self.x=150
        self.y=450
        #继承父类的构造方法
        super(HeroPlane, self).__init__(screen,'./picture/hero.png')
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
        if self.y > 0 and self.y <800:
            self.y+=50
        pass
    def moverUp(self):
        ''''上移动'''
        if self.y >0:
            self.y-=10
        pass
    #发射子弹
    def shoot(self):
        newBullet=CommonBullet(self.x,self.y,self.screen,'hero')
        self.bulletList.append(newBullet)
'''
2.创建子弹类
'''
#创建子弹基类
class CommonBullet():
    '''
    公共的子弹类
    '''
    def __init__(self,x,y,screen,bulletType):
        self.type=bulletType
        self.screen=screen
        self.x=x
        self.y=y
        if self.type == 'hero':
            self.x+=13
            self.y-=20
            self.imagepath='./picture/bullet.png'
            pass
        elif self.type == 'enemy':
            self.x=x
            self.y+=10
            self.imagepath='./picture/bullet1.png'
        self.image=pygame.image.load(self.imagepath)
    def move(self):
        '''
        子弹的移动
        :return:
        '''
        if self.type == 'hero':
            self.y-=2
        elif self.type == 'enemy':
            self.y+=2
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        '''
        判断子弹是否越界，我方子弹判断条件为y<0，敌机条件为y>500
        :return:
        '''
        if self.y < 0 or self.y > 500:
            return True
        else:
            return False
    pass

class Bullet(object):
    def __init__(self,x,y,screen):
        '''
        :param x:
        :param y:
        :param screen:
        '''
        self.x=x+20
        self.y=y-8
        self.screen=screen
        self.image=pygame.image.load('./picture/bullet.png')
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=3
        pass
    #增加自检，判断子弹是否越界
    def judge(self):
        if self.y < 0 :
            return True
        else:
            return False
    pass
'''
3.创建敌机类
'''
class EnemyPlay(BasePlane):
    def __init__(self,screen):
        #设置敌机的初始移动方向
        self.direction='right'
        self.x=0
        self.y=0
        super(EnemyPlay, self).__init__(screen,'./picture/enemy0.png')
    def shot(self):
        num=random.randint(1,20)
        if num==3:
            enemybullet=CommonBullet(self.x,self.y,self.screen,'enemy')
            self.bulletList.append(enemybullet)
    def move(self):
        if self.direction == 'right':
            self.x+=2
        elif self.direction == 'left':
            self.x-=2
        if self.x>350-20:
            self.direction='left'
        elif self.x <0:
            self.direction='right'
'''
4.创建敌机子弹类
'''
#直接继承BaseBullet即可，完成面向对象的编程。
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x=x
        self.y=y+5
        self.screen=screen
        self.image=pygame.image.load('./picture/bullet1.png')
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def move(self):
        self.y += 3
        pass
    # 增加自检，判断子弹是否越界
    def judge(self):
        if self.y > 500:
            return True
        else:
            return False


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
                Planobj.shoot()
                print('射了一发子弹')
def main():
    # 首先创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350, 500), 1, 35)
    # 创建一个背景图片对象
    background = pygame.image.load('./picture/background.png')
    # 设置一个title
    pygame.display.set_caption('飞机大战')
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./picture/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)  # 循环次数，-1表示无限循环
    # 创建一个飞机对象
    hero=HeroPlane(screen)
    #创建一个敌机对象
    enemyplay=EnemyPlay(screen)
    #设定要显示的内容
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        hero.display()
        #显示敌机
        enemyplay.display()
        enemyplay.move()
        enemyplay.shot()
        # 获取键盘事件
        keyboard_control(hero)
        # 更新显示内容
        pygame.display.update()
        #延迟
        #pygame.time.Clock().tick(20)
        pass
if __name__ == '__main__':
    main()
