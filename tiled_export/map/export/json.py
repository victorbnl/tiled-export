import dataclasses

from tiled_export import json


def export(tiledmap):

    # Get data
    data = dataclasses.asdict(tiledmap)

    # Convert to JSON
    result = json.Encoder(indent=2).encode(data)

    return result
