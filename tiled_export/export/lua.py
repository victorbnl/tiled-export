from dataclasses import is_dataclass

from tiled_export.export._common import Encoder, get_items
from tiled_export.types import *


class LuaEncoder(Encoder):

    def encode(self, obj, _depth=0):
        """Encode dictionary to Lua"""

        # Add "return" keyword at the beginning
        if _depth == 0:
            _depth += 1
            return "return " + self.encode(obj, _depth)

        # Color
        if isinstance(obj, Color):

            return "{" + ", ".join(self.encode(v, _depth) for v in (obj.r, obj.g, obj.b)) + "}"

        # Dataclass
        if is_dataclass(obj):

            content = self.separator().join(
                f"{k} = {self.encode(v, _depth)}"
                for k, v in get_items(obj)
                if v != None
            )

            return self.block(content, ("{", "}"))

        if isinstance(obj, list):

            content = self.separator().join(
                self.encode(v, _depth) for v in obj
            )

            return self.block(content, ("{", "}"))

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

        super().encode(obj)


def export(obj):
    """Exports Tiled object in Lua format"""

    # Export to Lua
    encoder = LuaEncoder(indent=2)
    result = encoder.encode(obj)

    return result
