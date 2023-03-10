"""
Command-line interface
"""


import argparse

from tiled_export.export import export


def main() -> None:
    """
    Exports your Tiled maps and tilesets in the desired format
    """

    # Parse arguments
    argparser = argparse.ArgumentParser(prog="Tiled Export", description="Exports your Tiled maps and tilesets in the desired format")
    argparser.add_argument("input_file", help="level project to export")
    argparser.add_argument("output_file", help="file to export data in")
    argparser.add_argument("-f", "--format", help="file to export data in")
    args = argparser.parse_args()

    # If not given, assume export format from output file extension
    if args.format:
        output_format = args.format
    else:
        output_format = args.output_file.split(".")[-1]

    # Export the files
    export(args.input_file, output_format, args.output_file)
