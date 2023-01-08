class Color(str):

    def __init__(self, hexcode):
        """A color"""

        self.hexcode = hexcode.lstrip('#')

    @classmethod
    def __get_validators__(cls):

        yield cls.validate

    @classmethod
    def validate(cls, v):

        if not isinstance(v, str):
            raise TypeError("String required")

        return cls(v)

    def hex(self):
        """Returns the color as an hex string"""

        return f"#{self.hexcode}"

    def rgb(self):
        """Returns the color as an RGB tuple"""

        r = int(self.hexcode[0:2], 16)
        g = int(self.hexcode[2:4], 16)
        b = int(self.hexcode[4:6], 16)

        return (r, g, b)
