class EventDispatcher:
    '''
    事件管理器。
    '''
    queue = []
    handles = {}

    @classmethod
    def attach(cls, name, handle):
        '''
        注册事件。
        '''
        cls.handles[name] = handle

    @classmethod
    def detach(cls, name):
        '''
        取消事件。
        '''
        if name in cls.handles:
            del cls.handles[name]

    @classmethod
    def emit(cls, name, data=None):
        '''
        发出事件。
        '''
        cls.queue.append((name, data))

    @classmethod
    def dispatch(cls, dt):
        '''
        调度事件。
        '''
        for (name, data) in cls.queue:
            if name in cls.handles:
                handler = cls.handles[name]
                handler(data)
        cls.queue.clear()
