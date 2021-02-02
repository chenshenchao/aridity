import os
import json
from pyglet import image
from pyglet.image import ImageGrid


class Image:
    '''
    图片资源
    '''

    data = {}
    meta = {}
    grids = {}

    @classmethod
    def get(cls, name, n=None):
        '''
        获取图片资源
        '''

        # 获取数据信息。
        if name not in cls.data:
            path = os.path.join('asset', '{}.png'.format(name))
            cls.data[name] = image.load(path)
        if n == None:
            return cls.data[name]

        # 获取数据元信息。
        if name not in cls.meta:
            p = os.path.join('asset', '{}.json'.format(name))
            if not os.path.isfile(p):
                raise Exception()
            with open(p, 'r', encoding='utf-8') as r:
                cls.meta[name] = json.load(r)

        # 加载切格图片。
        if name not in cls.grids:
            info = cls.meta[name]
            rows = info['rows']
            columns = info['columns']
            cls.grids[name] = ImageGrid(
                cls.data[name],
                rows=rows,
                columns=columns
            )
        if isinstance(n, int):
            return cls.grids[name][n]
        return [cls.grids[name][i] for i in n]
    