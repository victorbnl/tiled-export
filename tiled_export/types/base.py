"""
Basic structures Tiled types rely on
"""


from typing import Tuple
from pydantic_xml import BaseXmlModel, attr


class Point(BaseXmlModel, tag='point'):
    """
    A point
    """

    x: int = attr()
    y: int = attr()


class Color(str):
    """
    A color
    """

    def __init__(self, hexcode):

        self.hexcode = hexcode.lstrip('#')

    @classmethod
    def __get_validators__(cls):

        yield cls.validate

    @classmethod
    def validate(cls, v):

        if not isinstance(v, str):
            raise TypeError("String required")

        return cls(v)

    def hex(self) -> str:
        """
        Get the color as hexadecimal

        Returns:
            Hexadecimal string
        """

        return f"#{self.hexcode}"

    def rgb(self) -> Tuple[int, int, int]:
        """
        Get the color as RGB

        Returns:
            (r, g, b) tuple
        """

        r = int(self.hexcode[0:2], 16)
        g = int(self.hexcode[2:4], 16)
        b = int(self.hexcode[4:6], 16)

        return (r, g, b)
