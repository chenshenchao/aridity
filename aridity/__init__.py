import os
import sys
from pyglet import clock
from .event import EventDispatcher
from .view import MainWindow




def get_here():
    '''
    获取程序所在目录。
    '''
    path = os.path.realpath(sys.argv[0])
    return os.path.dirname(path)

window = MainWindow()
EventDispatcher.attach('close-window', lambda d: window.close())
clock.schedule_interval(EventDispatcher.dispatch, 1 / 120.0)