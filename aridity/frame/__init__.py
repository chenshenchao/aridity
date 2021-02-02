from pyglet import image
from pyglet import sprite
from pyglet.window import Window, FPSDisplay
from pyglet.window.key import F11
from glooey import Gui
from ..event import Event
from .actor import Actor


class MainWindow(Window):
    '''
    游戏主窗口。
    '''

    def __init__(self):
        super().__init__(visible=False)
        icon = image.load('aridity.ico')
        self.set_icon(icon)
        self.set_caption('蛮荒')
        self.gui = Gui(self)
        self.fps = FPSDisplay(window=self)
        

        self.actors = set()

    def add_actor(self, one):
        '''
        添加角色
        '''
        
        self.actors.add(one)

    def drop_actor(self, one):
        '''
        删除角色
        '''

        self.actors.remove(one)

    def clear_action(self):
        '''
        清空。
        '''

        self.actors.clear()

    def on_update(self, dt):
        '''
        更新
        '''
        for a in self.actors:
            a.on_update(dt)


    def on_draw(self):
        '''
        绘制事件
        '''
        self.fps.draw()
        
        # 角色绘制
        for a in self.actors:
            a.on_draw()

    def on_key_press(self, code, modifiers):
        '''
        键盘事件
        '''
        if code == F11:
            v = not self.fullscreen
            self.set_fullscreen(v)
        Event.emit('key-press', (code, modifiers, self))

    def on_mouse_press(self, x, y, button, modifiers):
        '''
        鼠标事件
        '''
        Event.emit('mouse-press', (x, y, button, modifiers, self))
