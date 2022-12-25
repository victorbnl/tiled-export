import csv
import io

from tiled_export.map.dataclasses import Tileset, TileLayer


def get_map_size(tiledmap):
    """Get total size of a map"""

    if not tiledmap.infinite:
        return (tiledmap.width, tiledmap.height)

    else:
        width, height = 0, 0
        for layer in tiledmap.layers:
            for chunk in layer.chunks:
                if chunk.x + chunk.width > width:
                    width = chunk.x + chunk.width
                if chunk.y + chunk.height > height:
                    height = chunk.y + chunk.height
        return (width, height)


def flatten(tiledmap):
    """Converts a layered tiledmap to a flat matrix"""

    map_width, map_height = get_map_size(tiledmap)

    result = [
        [
            -1
            for _ in range(map_width)
        ]
        for _ in range(map_height)
    ]

    # For each layer
    for layer in tiledmap.layers:
        # We want only tile layers
        if isinstance(layer, TileLayer):

            # Chunks
            if tiledmap.infinite:
                for chunk in layer.chunks:

                    # For each tile
                    for i, row in enumerate(chunk.data):
                        for j, gid in enumerate(row):
                            if gid != 0:

                                result[chunk.y+i][chunk.x+j] = gid

            # Data
            else:

                # For each tile
                for i, row in enumerate(layer.data):
                    for j, gid in enumerate(row):

                        result[j][i] = gid

    return result


def fix_gids(matrix, tilesets):
    """Fix the GIDs to make them comply with Tiled CSV export format"""

    # For each tile
    for i, row in enumerate(matrix):
        for j, gid in enumerate(row):
            if (gid != -1):

                # Get tile's tileset
                tileset = tilesets[0]
                for ts in tilesets:
                    if ts.firstgid > tileset.firstgid and gid >= ts.firstgid:
                        tileset = ts

                matrix[i][j] = gid - tileset.firstgid

    return matrix


def autocrop(matrix, max_left, max_right):
    """Crops a matrix of tiles to leave no space around the map"""

    crop_left = max_left
    crop_right = 0
    crop_top = max_right
    crop_bottom = 0

    # For each tile
    for i, row in enumerate(matrix):
        for j, gid in enumerate(row):

            # If tile is not empty
            if gid != -1:

                if j < crop_left:
                    crop_left = j

                if j > crop_right:
                    crop_right = j

                if i < crop_top:
                    crop_top = i

                if i > crop_bottom:
                    crop_bottom = i

    # Crop
    new_matrix = []
    for row in matrix[crop_top:crop_bottom+1]:
        new_matrix.append(row[crop_left:crop_right+1])

    return new_matrix


def export(tiledmap):
    """Exports a tilemap to CSV"""

    matrix = flatten(tiledmap)
    matrix = fix_gids(matrix, tiledmap.tilesets)
    matrix = autocrop(matrix, tiledmap.width, tiledmap.height)

    out = io.StringIO()
    csv.writer(out).writerows(matrix)

    return out.getvalue()
