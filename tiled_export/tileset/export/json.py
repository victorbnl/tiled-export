import dataclasses

from tiled_export import json


def export(tileset):

    data = dataclasses.asdict(tileset)
    jsoncontent = json.Encoder(indent=2).encode(data)

    return jsoncontent
