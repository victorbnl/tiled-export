"""
Export data to CSV
"""


import csv

from typing import List

from tiled_export.types import RootMap, Map, TileLayer, Chunk, EmbeddedTileset
from tiled_export.parse import parse_data
from tiled_export.convert.convert import VirtualFile


def get_chunks(layer: TileLayer) -> List[Chunk]:
    """
    Get every chunk of data from a layer

    Args:
        layer: Layer to get chunks from

    Returns:
        List of layer chunks
    """

    chunks = layer.chunks or []
    if layer.data:
        chunks.append(Chunk(data=layer.data, x=0, y=0, width=layer.width, height=layer.height))

    return chunks


def to_array(layer: TileLayer) -> List[List[int]]:
    """
    Converts a Tiled layer to a matrix

    Args:
        layer: Layer to build array from

    Returns:
        Matrix of GIDs
    """

    # Get layer size
    if not layer.chunks:
        layer_size = (layer.width, layer.height)
    else:
        left = right = top = bottom = 0
        for chunk in layer.chunks:
            left = min(left, chunk.x)
            right = max(right, chunk.x + chunk.width)
            top = min(top, chunk.y)
            bottom = max(bottom, chunk.y + chunk.height)
        layer_size = (right - left, bottom - top)

    # Get layer origin index
    x = y = 0
    if layer.chunks:
        for chunk in layer.chunks:
            x = min(x, chunk.x)
            y = min(y, chunk.y)
    x *= -1
    y *= -1
    origin = (x, y)

    # Create array of layer size
    array = [
        [
            -1
            for _ in range(layer_size[0])
        ]
        for _ in range(layer_size[1])
    ]

    # Write layer data in table
    for chunk in get_chunks(layer):
        parsed_data = parse_data(chunk.data, layer.encoding, layer.compression, chunk.width, chunk.height)
        for y, row in enumerate(parsed_data):
            for x, gid in enumerate(row):
                array[origin[1]+chunk.y+y][origin[0]+chunk.x+x] = gid

    # Crop to content if infinite map
    if not layer.data:
        crop_left = layer_size[0]
        crop_right = 0
        crop_top = layer_size[1]
        crop_bottom = 0
        for y, row in enumerate(array):
            for x, gid in enumerate(row):
                if gid > 0:
                    crop_left = min(crop_left, x)
                    crop_right = max(crop_right, x)
                    crop_top = min(crop_top, y)
                    crop_bottom = max(crop_bottom, y)
        array = [row[crop_left:crop_right+1] for row in array][crop_top:crop_bottom+1]

    return array


def fix_gids(array: List[List[int]], tilesets: List[EmbeddedTileset]) -> List[List[int]]:
    """
    Fix the GIDs to make them comply with Tiled's CSV format

    Args:
        array (list of lists of ints): Matrix to be fixed
        tilesets (list of tilesets): Level tilesets

    Returns:
        Fixed matrix
    """

    for y, row in enumerate(array):
        for x, gid in enumerate(row):
            if gid != 0:
                ts_firstgid = max([tileset.firstgid for tileset in tilesets if gid >= tileset.firstgid], default=-1)
                array[y][x] = gid - ts_firstgid
            else:
                array[y][x] = -1

    return array


def export(obj: RootMap, filename: str) -> List[VirtualFile]:
    """
    Converts a map to CSV files

    Args:
        obj: Object to export
        filename: Path to export object to

    Returns:
        List of virtual exported files

    Raises:
        ValueError: If `obj` is not a map
    """

    # Given object must be a map
    if not isinstance(obj, Map):
        raise ValueError("Map expected for conversion to CSV")

    # Convert each layer to arrays
    outfiles = []
    for layer in obj.layers:
        if isinstance(layer, TileLayer):
            array = fix_gids(to_array(layer), obj.tilesets)
            outfiles.append([layer.name, array])

    if len(outfiles) == 1:
        outfiles[0][0] = None

    # Return files
    files = []
    for suffix, content in outfiles:
        name, ext = filename.rsplit('.', 1)
        outfilename = name + (f"_{suffix}" if suffix else "") + f".{ext}"
        file_ = VirtualFile(path=outfilename)
        csv.writer(file_.io).writerows(content)
        files.append(file_)
    return files
