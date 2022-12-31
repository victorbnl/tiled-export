from dataclasses import dataclass


class Color:

    def __init__(self, hexcode):
        """A color"""

        self.hexcode = hexcode.lstrip("#")

    def hex(self):
        """Returns the color as an hex string"""

        return self.hexcode

    def rgb(self):
        """Returns the color as an RGB tuple"""

        r = int(self.hexcode[0:2], 16)
        g = int(self.hexcode[2:4], 16)
        b = int(self.hexcode[4:6], 16)

        return (r, g, b)
