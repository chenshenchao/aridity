import pyglet

class EventDispatcher:
    '''
    事件管理器。
    '''

    def __init__(self):
        '''
        '''

        self.queue = []
        self.handles = {}

    def attach(self, name, handle):
        '''
        注册事件。
        '''
        self.handles[name] = handle

    def detach(self, name):
        '''
        取消事件。
        '''
        if name in self.handles:
            del self.handles[name]

    def emit(self, name, data=None):
        '''
        发出事件。
        '''
        self.queue.append((name, data))

    def dispatch(self, dt):
        '''
        调度事件。
        '''
        for (name, data) in self.queue:
            if name in self.handles:
                handler = self.handles[name]
                handler(data)
        self.queue.clear()

dispatcher = EventDispatcher()
pyglet.clock.schedule_interval(dispatcher.dispatch, 1 / 120.0)
