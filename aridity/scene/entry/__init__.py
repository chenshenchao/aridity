from glooey import VBox
from .label import *
from .button import *
from ...event import Event
from ...frame import Actor


class EntryScene(VBox):
    '''
    开始场景。
    '''

    def __init__(self):
        super().__init__()
        self.alignment = 'center'
        title = MyTitle("蛮荒")
        self.add(title)
        buttons = [
            MyButton("新的开始", self.on_click_born),
            MyButton("旧的回忆", self.on_click_load),
            MyButton("绝迹蛮荒", self.on_click_quit),
        ]
        for button in buttons:
            self.add(button)

        self.mon = Actor()
        Event.emit('add-actor', self.mon)

    def on_click_born(self):
        '''
        创建角色。
        '''
        Event.emit('swap-scene', 'born')

    def on_click_load(self):
        '''
        读取存档。
        '''
        Event.emit('swap-scene', 'world')

    def on_click_quit(self):
        '''
        退出游戏。
        '''
        Event.emit('close-window')
