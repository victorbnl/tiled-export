import csv

from tiled_export.types import Map, TileLayer, Chunk
from tiled_export.parse import parse_data


def get_chunks(layer):
    """Get every chunk of data from a layer"""

    chunks = layer.chunks or []
    if layer.data:
        chunks.append(Chunk(data=layer.data, x=0, y=0, width=layer.width, height=layer.height))

    return chunks


def to_array(layer):
    """Converts a Tiled layer to a list of lists of ints"""

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


def fix_gids(array, tilesets):
    """Fix the GIDs to make them comply with Tiled's CSV format"""

    for y, row in enumerate(array):
        for x, gid in enumerate(row):
            if gid != 0:
                ts_firstgid = max([tileset.firstgid for tileset in tilesets if gid >= tileset.firstgid], default=-1)
                array[y][x] = gid - ts_firstgid
            else:
                array[y][x] = -1

    return array


def export(obj, filename):
    """Exports a Tiled map to a CSV file"""

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

    # Write files
    for suffix, content in outfiles:
        name, ext = filename.rsplit('.', 1)
        outfilename = name + (f"_{suffix}" if suffix else "") + f".{ext}"
        with open(outfilename, 'w') as outfile:
            csv.writer(outfile).writerows(content)
