from pyglet.sprite import Sprite
from ..asset import Image
from ..archive.role import Role

class Actor:
    '''
    游戏对象。
    '''

    def __init__(self):
        '''
        初始化。
        '''

        self.imgs = Image.get('characters', [0, 1, 2])
        self.role = Role()
        self.timeline = 0.0
        self.sprite = Sprite(self.imgs[0])
        self.sprite.x = 100
        self.sprite.y = 100
        self.role.x = 100
        self.role.y = 100

    def on_update(self, dt):
        '''
        更新事件。
        '''
        self.timeline = (self.timeline + dt) % 1
        i = int((self.timeline * 3) % 3)
        self.sprite.image = self.imgs[i]
        self.sprite.x = self.role.x
        self.sprite.y = self.role.y

    def on_draw(self):
        '''
        绘图事件
        '''

        self.sprite.draw()
