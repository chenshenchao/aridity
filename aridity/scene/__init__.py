from ..event import Event
from ..frame import MainWindow
from .born import BornScene
from .entry import EntryScene
from .world import WorldScene


class Scene:
    '''
    场景调度器。
    '''

    window = MainWindow()
    scenes = {
        'born': BornScene,
        'entry': EntryScene,
        'world': WorldScene,
    }

    @classmethod
    def init(cls, scene):
        '''
        初始化。
        '''
        cls.window.set_visible(True)
        cls.swap(scene)
        Event.attach('swap-scene', cls.swap)
        Event.attach('add-actor', cls.add_actor)
        Event.attach('close-window', lambda d: cls.window.close())

    @classmethod
    def add_actor(cls, one):
        cls.window.add_actor(one)

    @classmethod
    def on_update(cls, dt):
        '''
        刷新。
        '''
        cls.window.on_update(dt)

    @classmethod
    def clear(cls):
        '''
        清空场景。
        '''
        cls.window.gui.clear()
        

    @classmethod
    def swap(cls, name):
        '''
        切换场景。
        '''
        cls.window.gui.clear()
        action = cls.scenes[name]
        cls.window.gui.add(action())
