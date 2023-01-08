from importlib import import_module

from typing import Literal

from tiled_export.parse import parse_file


def convert(src_filename: str, format: Literal['csv', 'json', 'lua'], dest_filename: str):
    """Converts the file with given filename to given format"""

    obj = parse_file(src_filename)

    exporter = import_module(f"tiled_export.export.{format}")
    result = exporter.export(obj, dest_filename)

    return result
