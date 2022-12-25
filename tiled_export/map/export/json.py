import dataclasses

from tiled_export import json
from tiled_export.map.parse_data import parse_data


def expand_data(dictmap):
    """Convert raw layer data to array"""

    for i, layer in enumerate(dictmap["layers"]):
        if dictmap["infinite"]:
            for j, chunk in enumerate(layer["chunks"]):
                dictmap["layers"][i]["chunks"][j]["data"] = parse_data(chunk["data"], layer["encoding"], layer["compression"], chunk["width"], chunk["height"])
        else:
            dictmap["layers"][i]["data"] = parse_data(layer["data"], layer["encoding"], layer["compression"], layer["width"], layer["height"])

    return dictmap


def strip_none(obj):
    """Removes all None values from dictionary (recursive)"""

    if isinstance(obj, list):

        for i, v in enumerate(obj):
            obj[i] = strip_none(v)

        return obj

    elif isinstance(obj, dict):

        for i, (k, v) in enumerate(list(obj.items())):

            if isinstance(v, list):
                obj[k] = strip_none(v)

            if isinstance(v, dict):
                obj[k] = strip_none(v)

            if v == None:
                obj.pop(k)

    return obj


def export(tiledmap):
    """Exports a tiledmap to JSON"""

    # Get data
    dictmap = dataclasses.asdict(tiledmap)

    dictmap = expand_data(dictmap)
    dictmap = strip_none(dictmap)

    # Convert to JSON
    result = json.Encoder(indent=2).encode(dictmap)

    return result
