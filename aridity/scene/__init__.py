from ..event import Event
from .view import MainWindow
from .born import BornScene
from .entry import EntryScene
from .world import WorldScene


class Scene:
    '''
    场景调度器。
    '''

    window = None
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
        cls.window = MainWindow()
        cls.swap(scene)
        Event.attach('swap-scene', cls.swap)
        Event.attach('close-window', lambda d: cls.window.close())

    @classmethod
    def swap(cls, name):
        '''
        切换场景。
        '''
        cls.window.gui.clear()
        action = cls.scenes[name]
        cls.window.gui.add(action())
