from .. import window
from ..event import dispatcher
from .born import BornScene
from .entry import EntryScene
from .world import WorldScene

scenes = {
    'born': BornScene,
    'entry': EntryScene,
    'world': WorldScene,
}

def swap_scene(name):
    window.gui.clear()
    cls = scenes[name]
    window.gui.add(cls())


dispatcher.attach('swap-scene', swap_scene)
