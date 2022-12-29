from importlib import import_module

from tiled_export.parse import parse


def convert(filename, format):
    """Converts the file with given filename to given format"""

    # Get Tiled object
    obj = parse(filename)

    # Export it
    result = import_module(f"tiled_export.export.{format}").export(obj)

    return result
