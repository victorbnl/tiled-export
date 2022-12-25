import argparse
import importlib

from tiled_export import utils

from tiled_export.map.convert import convert_map
from tiled_export.tileset.convert import convert_tileset


def main():
    """Exports your Tiled maps and tilesets in the desired format"""

    # Parse arguments
    argparser = argparse.ArgumentParser(prog="Tiled Export", description="Exports your Tiled maps and tilesets in the desired format")
    argparser.add_argument("input_file", help="level project to export")
    argparser.add_argument("output_file", help="file to export data in")
    argparser.add_argument("-f", "--format", help="file to export data in")
    args = argparser.parse_args()

    # Check if map or tileset
    input_format = utils.get_file_ext(args.input_file)

    # If not given, assume export format from output file extension
    if args.format:
        output_format = args.format
    else:
        output_format = utils.get_file_ext(args.output_file)

    # Convert the file
    if input_format == "tmx":
        result = convert_map(args.input_file, output_format)
    elif input_format == "tsx":
        result = convert_tileset(args.input_file, output_format)
    else:
        raise ValueError(f"Invalid input file format: {input_format}")

    # Write output
    with open(args.output_file, 'w') as ofstream:
        ofstream.write(result)
