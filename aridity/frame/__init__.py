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
        self.set_caption('索然')
        self.gui = Gui(self)
        self.fps = FPSDisplay(window=self)

        self.a = Actor()

    def on_draw(self):
        '''
        绘制事件
        '''
        self.fps.draw()
        self.a.on_draw()

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
