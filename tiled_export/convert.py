from importlib import import_module

from tiled_export.parse import parse


def convert(source_file, format, dest_file):
    """Converts the file with given filename to given format"""

    obj = parse(source_file)

    exporter = import_module(f"tiled_export.export.{format}")
    result = exporter.export(obj, dest_file)

    return result
