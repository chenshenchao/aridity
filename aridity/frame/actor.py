from pyglet.sprite import Sprite
from ..asset import Image

class Actor:
    '''
    游戏对象。
    '''

    def __init__(self):
        i = Image.get('characters', 0)
        self.sprite = Sprite(i)
        self.sprite.x = 100
        self.sprite.y = 100

    def on_draw(self):
        '''
        绘图事件
        '''
        self.sprite.draw()
