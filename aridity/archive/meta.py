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
