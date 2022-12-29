from dataclasses import dataclass


@dataclass
class Color:

    r: int = 0
    g: int = 0
    b: int = 0

    def __init__(self, hexcode):

        hexcode = hexcode.lstrip("#")

        r_hex = hexcode[0:2]
        g_hex = hexcode[2:4]
        b_hex = hexcode[4:6]

        self.r = int(r_hex, 16)
        self.g = int(g_hex, 16)
        self.b = int(b_hex, 16)
