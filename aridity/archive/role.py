from dataclasses import dataclass
from .meta import XYZ, JMSHT

@dataclass
class Role:
    '''
    角色类
    '''

    position: XYZ = XYZ()

    hp: float = 100.0
    hp_max: float = 100.0
    mp: float = 100.0
    mp_max: float = 100.0

    

