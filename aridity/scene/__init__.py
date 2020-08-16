from .. import window
from ..event import EventDispatcher
from .born import BornScene
from .entry import EntryScene
from .world import WorldScene

scenes = {
    'born': BornScene,
    'entry': EntryScene,
    'world': WorldScene,
}

def get_scene(name):
    return scenes[name]

def swap_scene(name):
    window.gui.clear()
    cls = scenes[name]
    window.gui.add(cls())


EventDispatcher.attach('swap-scene', swap_scene)
