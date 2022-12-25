import importlib

from tiled_export.map.parse_map import parse_map


def convert_map(filename, format):

    tiledmap = parse_map(filename)
    result = importlib.import_module(f"tiled_export.map.export.{format}").export(tiledmap)

    return result
