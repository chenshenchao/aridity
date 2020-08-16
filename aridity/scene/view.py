from pyglet.window import Window, FPSDisplay
from pyglet import image
from pyglet import sprite
from glooey import Gui

class MainWindow(Window):
    '''
    游戏主窗口。
    '''

    def __init__(self):
        super().__init__()
        self.set_caption('索然')
        self.gui = Gui(self)
        self.fps = FPSDisplay(window=self)
        self.a = image.load('asset/characters.png')
        self.grid = image.ImageGrid(self.a, 8, 12)
        icon = image.load('aridity.ico')
        self.set_icon(icon)
        self.s = sprite.Sprite(self.grid[0])
        
        self.s.x = 100
        self.s.y = 100

    def on_draw(self):
        '''
        绘制事件
        '''
        self.fps.draw()
        self.s.draw()

    def on_key_press(self, code, modifiers):
        '''
        键盘事件
        '''
        print(code)

    def on_mouse_press(self, x, y, button, modifiers):
        '''
        鼠标事件
        '''
        print('({}, {}) {} {}'.format(x, y, button, modifiers))