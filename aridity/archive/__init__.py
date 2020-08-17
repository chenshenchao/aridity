import os
from ..system import get_here

def get_save_path():
    '''
    获取保存目录。
    '''
    here = get_here()
    return os.path.join(here, 'save')

def has_save():
    folder = get_save_path()
    path = os.path.join(folder, 'main.json')
    return os.path.isfile(path)