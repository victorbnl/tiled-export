import json

from pydantic import BaseModel

from tiled_export.export._common import Encoder
from tiled_export.types import *
from tiled_export.parse_data import parse_data


class RowList(list):
    pass


def to_dict(obj, _state={}):
    """Converts a Tiled type to a dictionary"""

    # Fix csv -> no encoding
    if _state.get("field_name", None) == "encoding" and obj == "csv":
        return None

    # Parse data
    if _state.get("field_name", None) == "data" and _state["data_encoding"] == "csv" and obj != None:
        return RowList(parse_data(obj, encoding="csv"))

    # Get layer encoding
    if isinstance(obj, TileLayer):
        _state["data_encoding"] = obj.encoding

    # Color
    if isinstance(obj, Color):
        return obj.hex()

    # Pydantic class
    types = {Map: "map"}
    if isinstance(obj, BaseModel):
        return {
            k: v
            for k, v in [
                [k.rstrip("_"), to_dict(v, _state | {"field_name": k})]
                for k, v in obj
                if v != None
            ]
            if v != None
        } | ({"type": types[type(obj)]} if type(obj) in types else {})

    # List
    if isinstance(obj, list):
        return [to_dict(v, _state) for v in obj]

    # Other types
    else:
        return obj


class JsonEncoder(Encoder):

    def encode(self, obj, _state={}):
        """Encodes an object into a JSON string"""

        # Dictionary
        if isinstance(obj, dict):
            return self.block(
                self.separator().join(
                    f"\"{k}\": {v}"
                    for k, v in [
                        [k, self.encode(v)]
                        for k, v in obj.items()
                    ]
                ),
                ("{", "}")
            )

        # Row list
        if isinstance(obj, RowList):
            return self.block(
                ",\n".join(
                    ", ".join(
                        self.encode(v)
                        for v in line
                    )
                    for line in obj
                ),
                ("[", "]")
            )

        # List
        if isinstance(obj, list):
            return self.block(
                self.separator().join(
                    self.encode(v)
                    for v in obj
                ),
                ("[", "]")
            )

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
            obj = obj.replace('/', '\/')
            return f"\"{obj}\""

        super().encode(obj)


def export(obj, filename):
    """Exports a Tiled object to a JSON file"""

    dict_ = to_dict(obj)

    encoder = JsonEncoder(indent=2)
    result = encoder.encode(dict_)

    with open(filename, 'w') as jsonfile:
        jsonfile.write(result + "\n")
