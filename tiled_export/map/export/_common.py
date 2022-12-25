import dataclasses
from dataclasses import fields

from tiled_export.map.parse_data import parse_data
from tiled_export.map.dataclasses import *


def tiledmap_to_dict(obj, _layer=None, _field_name=None):
    """Convert tiledmap to dictionary (recursive)"""

    # Layers
    if isinstance(obj, TileLayer):
        _layer = obj

    # Lists
    if isinstance(obj, list):
        return [tiledmap_to_dict(v, _layer) for v in obj]

    # Dataclasses
    if dataclasses.is_dataclass(obj):
        dict_ = {}
        for field in fields(obj):
            k, v = field.name, getattr(obj, field.name)
            k = k.rstrip("_")
            if v != None:
                dict_[k] = tiledmap_to_dict(v, _layer, field.name)
        return dict_

    # Data field
    if _field_name == "data" and _layer.encoding == "csv":
        return parse_data(obj, _layer.encoding, _layer.compression, _layer.width, _layer.height)

    return obj
