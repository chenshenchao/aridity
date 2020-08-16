from pyglet import app
from pyglet.clock import schedule_interval
from aridity.event import Event
from aridity.scene import Scene

def on_update(dt):
    '''
    游戏循环的主体。
    '''
    Event.dispatch(dt)

schedule_interval(on_update, 1 / 120.0)
Scene.init('entry')
app.run()
