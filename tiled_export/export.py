"""
Export Tiled files
"""


from typing import List, Literal

from tiled_export.convert.convert import VirtualFile, convert
from tiled_export.parse import parse_file


def convert_file(input_file: str, format: Literal['csv', 'json', 'lua'], output_file: str) -> List[VirtualFile]:
    """
    Converts a Tiled file to a list of virtual files

    Args:
        input_file (string): File to read content from
        format (literal): Format to export the project into
        output_file (str): Path of the file to export the project into

    Returns:
        List of virtual exported files
    """

    obj = parse_file(input_file)

    return convert(obj, format, output_file)


def export(input_file: str, format: Literal['csv', 'json', 'lua'], output_file: str) -> None:
    """
    Exports a Tiled file to and output file

    Args:
        input_file (string): Path of the input file to read content from
        format (literal): Format to export the project to
        output_file (string): Path of the output file to export to
    """

    files = convert_file(input_file, format, output_file)

    for virtual_file in files:
        with open(virtual_file.path, 'w') as outfile:
            outfile.write(virtual_file.get_content())
