from dataclasses import is_dataclass

from tiled_export.export._common import Encoder, get_items
from tiled_export.types import *


class JsonEncoder(Encoder):

    def encode(self, obj, _data_encoding=None):
        """Encodes an object into a JSON string"""

        # Dataclass
        if is_dataclass(obj):

            content = self.separator().join(
                f"\"{k}\": {self.encode(v, _data_encoding)}"
                for k, v in get_items(obj)
                if v != None
            )

            return self.block(content, ("{", "}"))

        # List
        if isinstance(obj, list):

            content = self.separator().join(
                self.encode(v, _data_encoding) for v in obj
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


def export(obj):
    """Exports a Tiled object to JSON"""

    # Convert Tiled object to dictionary
    encoder = JsonEncoder(indent=2)
    result = encoder.encode(obj)

    return result
