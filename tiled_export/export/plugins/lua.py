from pydantic import BaseModel

from typing import Union, Dict, List, Any

from tiled_export.export.common import Encoder
from tiled_export.types import *
from tiled_export.parse.parse_data import parse_data
from tiled_export.export.result_file import ResultFile


class InlineList(list):
    pass


class RowList(list):
    pass


def to_dict(obj: Any, _state: Dict[str, Any] = {}) -> Any:
    """Converts a Tiled type to a dictionary"""

    # Fix csv -> lua encoding
    if _state.get('field_name', None) == 'encoding' and obj == 'csv':
        return to_dict('lua', _state)

    # No compression when encoding is csv
    if _state.get('field_name', None) == 'compression' and _state.get('data_encoding', None) == 'csv':
        return None

    # Parse data
    if _state.get('field_name', None) == 'data' and _state['data_encoding'] == 'csv' and obj != None:
        return RowList(parse_data(obj, encoding='csv'))

    # Get layer encoding
    if isinstance(obj, TileLayer):
        _state['data_encoding'] = obj.encoding

    # Color
    if isinstance(obj, Color):
        return InlineList(obj.rgb())

    # Pydantic class
    if isinstance(obj, BaseModel):

        res = {}
        for k, v in obj:
            k = k.rstrip('_')
            v = to_dict(v, {**_state, 'field_name': k})

            # Fix tileset source -> filename
            if isinstance(obj, Tileset) and k == 'source':
                k = 'filename'

            res[k] = v

        return res

    # List
    if isinstance(obj, list):
        return [to_dict(v, _state) for v in obj]

    # Other types
    else:
        return obj


class LuaEncoder(Encoder):

    def encode(self, obj: Any, _depth: int = 0) -> str:
        """Encodes object to Lua string"""

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
                        if v not in (None, [])
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
                ("{", "}")
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

        return super().encode(obj)


def export(obj: Union[RootMap, RootTileset], filename: str) -> List[ResultFile]:
    """Exports a Tiled object to a Lua file"""

    dict_ = to_dict(obj)

    dict_['luaversion'] = "5.1"

    encoder = LuaEncoder(indent=2)
    result = encoder.encode(dict_)

    result_file = ResultFile(filename)
    result_file.write(result)

    return [result_file]
