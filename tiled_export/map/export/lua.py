import dataclasses

from tiled_export.map.export._common import *
from tiled_export.utils import hex_to_rgb


class LuaEncoder():

    def __init__(self, indentation):
        """Dictionary to Lua encoder"""

        self.indentation = indentation
        self.newline = "\n" if self.indentation > 0 else " "

    def indent(self, string):
        """Add a level of indentation to a string"""

        return "".join((self.indentation * " ") + line for line in string.splitlines(True))

    def encode(self, obj, _depth=0):
        """Encode dictionary to Lua"""

        # Add "return" keyword at the beginning
        if _depth == 0:
            _depth += 1
            return "return " + self.encode(obj, _depth)

        # Dictionary
        if isinstance(obj, dict):

            content = ""
            for i, (k, v) in enumerate(obj.items()):
                suffix = f",{self.newline}" if i != len(obj) - 1 else ""
                v = self.encode(v, _depth)
                content += f"{k} = {v}{suffix}"

            string = "{" + self.newline
            string += self.indent(content)
            string += self.newline + "}"

            return string

        # List or tuple
        if isinstance(obj, list) or isinstance(obj, tuple):

            # Matrix
            if all([isinstance(v, list) for v in obj]):

                content = ""
                for i, row in enumerate(obj):
                    for j, element in enumerate(row):
                        # separator = ", " if i != len(obj) - 1 or j != len(row) - 1 else ""
                        separator = ""
                        if i != len(obj) - 1 or j != len(row) - 1:
                            separator += ","
                            if j != len(row) - 1:
                                separator += " "
                        content += f"{element}{separator}"
                    content += self.newline

                string = "{" + self.newline
                string += self.indent(content)
                string += "}"

                return string

            # Normal list
            else:

                content = ""
                for i, v in enumerate(obj):
                    suffix = f",{self.newline}" if i != len(obj) - 1 else ""
                    v = self.encode(v, _depth)
                    content += f"{v}{suffix}"
                content = self.indent(content)

                string = "{" + self.newline
                string += content
                string += self.newline + "}"

                return string

        # Boolean
        if isinstance(obj, bool):
            return "true" if obj else "false"

        # Float
        if isinstance(obj, float):
            return str(obj)

        # Integer
        if isinstance(obj, int):
            return str(obj)

        # String
        if isinstance(obj, str):
            return f"\"{obj}\""

        # None
        if obj == None:
            return "nil"

        raise ValueError("Can't encode type: " + type(obj).__name__)


def export(tiledmap):
    """Export tiledmap in Lua format"""

    dictmap = tiledmap_to_dict(tiledmap)

    dictmap["backgroundcolor"] = hex_to_rgb(tiledmap.backgroundcolor)

    encoder = LuaEncoder(indentation=2)
    result = encoder.encode(dictmap)

    print(result)
    return result
