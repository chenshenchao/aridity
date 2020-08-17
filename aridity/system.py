import os
import sys


def get_here():
    '''
    获取程序所在目录。
    '''
    path = os.path.realpath(sys.argv[0])
    return os.path.dirname(path)