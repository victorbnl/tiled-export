"""
Serialize Tiled objects
"""


import io
from importlib import import_module

from typing import List, Literal

from tiled_export.parse import parse_file
from tiled_export.types import RootMap, RootTileset


class VirtualFile:
    """
    Represents a file yet to be written
    """

    def __init__(self, path):

        self.path = path
        self.io = io.StringIO()

    def write(self, content: str) -> None:
        """
        Writes content into result file

        Args:
            content (string): Text to be written
        """

        self.io.write(content)

    def get_content(self) -> str:
        """
        Get file content

        Returns:
            File content
        """

        return self.io.getvalue()


def convert(obj: RootMap | RootTileset, format: Literal['csv', 'json', 'lua'], dest_filename: str) -> List[VirtualFile]:
    """
    Converts a Tiled object to files

    Args:
        obj (Map or Tileset): Object to convert
        format (string): Format to convert the file into
        dest_filename (string): Name of the file to export to

    Returns:
        A list of converted virtual files
    """

    exporter = import_module(f'tiled_export.convert.plugins.{format}')
    result_files = exporter.export(obj, dest_filename)

    return result_files
