from . import Image

class Animation2D:
    '''
    2D 帧动画。
    '''

    def __init__(self):
        '''
        初始化。
        '''

        self.time = 1
        self.frames = []

    def add_frame(self, one):
        '''
        添加帧。
        '''

        self.frames.append(one)
        self.frames.sort(key=lambda k: k[0])

    def get_frame(self, dt):
        '''
        获取关键帧。
        '''

        count = len(self.frames)
        if count == 0:
            return None
        if count == 1:
            return self.frames[0]
        t = (t + dt) % self.time
        for i in range(count - 1):
            k = self.frames[i][0]
            n = self.frames[i + 1][0]
            if k < t and n > t:
                return self.frames[i]
        return self.frames[n]
    
    @classmethod
    def from_meta(cls, meta):
        '''
        '''
        r = cls()
        r.time = meta['time']
        for d in meta['frames']:
            t = d['time']
            i = Image.get(
                d['name'],
                'n' in d if d['n'] else None
            )
            r.frames.append((t, i))
        return r



class Model2D:
    '''
    2D 模型。
    '''

    def __init__(self):
        '''
        '''
        self.action = None
        self.speed = 1
        self.actions = {}
        self.timeline = 0

    def set_action(self, name, start=0):
        '''
        切换动画
        '''
        self.action = self.actions[name]
        self.timeline = start

    def on_update(self, dt):
        '''
        更新动画。
        '''
