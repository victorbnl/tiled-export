from pydantic import BaseModel

from tiled_export.export._common import Encoder
from tiled_export.types import *
from tiled_export.parse_data import parse_data


class InlineList(list):
    pass


class RowList(list):
    pass


def to_dict(obj, _state={}):
    """Converts a Tiled type to a dictionary"""

    # Parse data
    if _state.get("field_name", None) == "data" and _state["data_encoding"] == "csv":
        return RowList(parse_data(obj, encoding="csv"))

    # Get layer encoding
    if isinstance(obj, TileLayer):
        _state["data_encoding"] = obj.encoding

    # Color
    if isinstance(obj, Color):
        return InlineList(obj.rgb())

    # Pydantic class
    if isinstance(obj, BaseModel):
        return {
            k: to_dict(v, _state | {"field_name": k})
            for k, v in [
                [k.rstrip("_"), v]
                for k, v in obj
            ]
        }

    # List
    if isinstance(obj, list):
        return [to_dict(v, _state) for v in obj]

    # Other types
    else:
        return obj


class LuaEncoder(Encoder):

    def encode(self, obj, _depth=0):
        """Encode dictionary to Lua"""

        # Add "return" keyword at the beginning
        if _depth == 0:
            _depth += 1
            return "return " + self.encode(obj, _depth)

        # Dictionary
        if isinstance(obj, dict):

            return self.block(
                self.separator().join(
                    f"{k} = {v}"
                    for k, v in [
                        [k, self.encode(v, _depth)]
                        for k, v in obj.items()
                        if v != None
                    ]
                ),
                ("{", "}")
            )

        # Row list
        if isinstance(obj, RowList):
            return self.block(
                ",\n".join(
                    ", ".join(
                        self.encode(v, _depth)
                        for v in line
                    )
                    for line in obj
                ),
                ("[", "]")
            )

        # Inline list
        if isinstance(obj, InlineList):
            return "{" + ", ".join([self.encode(v, _depth) for v in obj]) + "}"

        # List
        if isinstance(obj, list):
            return self.block(
                self.separator().join(
                    self.encode(v, _depth)
                    for v in obj
                ),
                ("{", "}")
            )

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


def export(obj, filename):
    """Exports a Tiled object to a Lua file"""

    dict_ = to_dict(obj)

    encoder = LuaEncoder(indent=2)
    result = encoder.encode(dict_)

    with open(filename, 'w') as luafile:
        luafile.write(result + "\n")
