from importlib import import_module

from typing import List, Literal
from tiled_export.export.result_file import ResultFile

from tiled_export.parse import parse_file


def convert(src_filename: str, format: Literal['csv', 'json', 'lua'], dest_filename: str) -> List[ResultFile]:
    """Converts the file with given filename to given format"""

    obj = parse_file(src_filename)

    exporter = import_module(f'tiled_export.export.plugins.{format}')
    result_files = exporter.export(obj, dest_filename)

    return result_files
