from pydantic import BaseModel

from tiled_export.export._common import Encoder, get_items
from tiled_export.types import *
from tiled_export.parse_data import parse_data


class LuaEncoder(Encoder):

    def encode(self, obj, _depth=0, _state={}):
        """Encode dictionary to Lua"""

        # Add "return" keyword at the beginning
        if _depth == 0:
            _depth += 1
            return "return " + self.encode(obj, _depth)

        # Layer (get encoding)
        if isinstance(obj, TileLayer):
            _state["data_encoding"] = obj.encoding

        # Data (parse it)
        if isinstance(obj, str) and _state.get("field_name", None) == "data" and _state["data_encoding"] == "csv":

            parsed = parse_data(obj, encoding="csv")

            content = ",\n".join(
                ", ".join(
                    self.encode(v, _depth, _state)
                    for v in line
                )
                for line in parsed
            )

            return self.block(content, ("{", "}"))

        # Color
        if isinstance(obj, Color):

            return "{" + ", ".join(self.encode(v, _depth, _state) for v in obj.rgb()) + "}"

        # Dataclass
        if issubclass(type(obj), BaseModel):

            lines = []
            for k, v in get_items(obj):
                if v != None:
                    _state["field_name"] = k
                    lines.append(f"{k} = {self.encode(v, _depth, _state)}")
            _state["field_name"] = None
            content = self.separator().join(lines)

            return self.block(content, ("{", "}"))

        # List
        if isinstance(obj, list):

            content = self.separator().join(
                self.encode(v, _depth, _state) for v in obj
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
