from dataclasses import dataclass


@dataclass
class XYZ:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class JMSHT:
    j: float = 1.0
    m: float = 1.0
    s: float = 1.0
    h: float = 1.0
    t: float = 1.0


@dataclass
class HM:
    hp: float = 100.0
    max_hp: float = 100.0
    mp: float = 100.0
    max_mp: float = 100.0
