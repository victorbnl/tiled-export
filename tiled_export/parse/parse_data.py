import csv
import base64
import gzip
import zlib
import zstd
import struct

from typing import List, Literal

formats = ['csv', 'base64']

def parse_data(
    data: str,
    encoding: Literal['csv', 'base64'] = 'csv',
    compression: Literal['', 'gzip', 'zlib', 'zstd'] = '',
    width: int = 16,
    height: int = 16
) -> List[List[int]]:
    """Parses a Tiled data block with given encoding and compression"""

    data = data.strip()

    # Parse CSV
    if encoding == "csv":
        rows = [row.rstrip(", ") for row in data.splitlines()]
        parsed = [[int(gid) for gid in row] for row in csv.reader(rows)]

    # Parse base64
    if encoding == "base64":

        parsed = [
            [
                -1
                for _ in range(width)
            ]
            for _ in range(height)
        ]

        # Decode base64
        bytes_array = base64.b64decode(data)

        # No compression
        if compression == "":
            array = bytes_array

        # Gzip compression
        if compression == "gzip":
            array = gzip.decompress(bytes_array)

        # zlib compression
        if compression == "zlib":
            array = zlib.decompress(bytes_array)

        # Zstandard compression
        if compression == "zstd":
            array = zstd.ZSTD_uncompress(bytes_array)

        # Decode values
        length = width*height
        values = struct.unpack(f"<{length}I", array)

        # Separate lines
        for i, v in enumerate(values):
            parsed[i//width][i%width] = v

    return parsed
