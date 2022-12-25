import importlib

from tiled_export.tileset.parse import parse_tileset


def convert_tileset(filename, format):

    tileset = parse_tileset(filename)
    result = importlib.import_module(f"tiled_export.tileset.export.{format}").export(tileset)

    return result
