from pydantic import BaseModel

from tiled_export.export._common import Encoder, get_items
from tiled_export.types import *
from tiled_export.parse_data import parse_data


class JsonEncoder(Encoder):

    def encode(self, obj, _state={}):
        """Encodes an object into a JSON string"""

        # Add type: map if it's a map
        if isinstance(obj, Map):
            obj.type_ = "map"

        # Data (parse it)
        if isinstance(obj, str) and _state.get("field_name", None) == "data" and _state["encoding"] == "csv":

            parsed = parse_data(obj, encoding="csv")

            content = ",\n".join(
                ", ".join(
                    self.encode(v, _state)
                    for v in line
                )
                for line in parsed
            )

            return self.block(content, ("[", "]"))

        # Layer (get encoding)
        if isinstance(obj, TileLayer):
            _state["encoding"] = obj.encoding

        # Color
        if isinstance(obj, Color):
            return self.encode(obj.hex(), _state)

        # Dataclass
        if issubclass(type(obj), BaseModel):

            lines = []
            for k, v in get_items(obj):
                if v != None:
                    _state["field_name"] = k
                    lines.append(f"\"{k}\": {self.encode(v, _state)}")
            _state["field_name"] = None
            content = self.separator().join(lines)

            return self.block(content, ("{", "}"))

        # List
        if isinstance(obj, list):

            content = self.separator().join(
                self.encode(v, _state) for v in obj
            )

            return self.block(content, ("[", "]"))

        # Boolean
        if isinstance(obj, bool):
            return "true" if obj else "false"

        # Integer
        if isinstance(obj, int):
            return str(obj)

        # Float
        if isinstance(obj, float):
            return str(obj)

        # String
        if isinstance(obj, str):
            return f"\"{obj}\""

        super().encode(obj)


def export(obj, filename):
    """Exports a Tiled object to a JSON file"""

    # Convert Tiled object to JSON
    encoder = JsonEncoder(indent=2)
    result = encoder.encode(obj)

    # Write file
    with open(filename, 'w') as jsonfile:
        jsonfile.write(result)
