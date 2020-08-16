import os
import sys
from pyglet import clock
from .event import Event




def get_here():
    '''
    获取程序所在目录。
    '''
    path = os.path.realpath(sys.argv[0])
    return os.path.dirname(path)

clock.schedule_interval(Event.dispatch, 1 / 120.0)