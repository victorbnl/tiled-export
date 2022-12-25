import dataclasses

from tiled_export import json
from tiled_export.map.export._common import *


def export(tiledmap):
    """Exports a tiledmap to JSON"""

    # Get data
    dictmap = tiledmap_to_dict(tiledmap)

    # Convert to JSON
    result = json.Encoder(indent=2).encode(dictmap)

    return result
