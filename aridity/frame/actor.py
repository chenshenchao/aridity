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

        i = Image.get('characters', 0)
        self.role = Role()
        self.sprite = Sprite(i)
        self.sprite.x = 100
        self.sprite.y = 100

    def on_update(self, dt):
        '''
        更新事件。
        '''
        self.sprite.x = self.role.x
        self.sprite.y = self.role.y

    def on_draw(self):
        '''
        绘图事件
        '''

        self.sprite.draw()
