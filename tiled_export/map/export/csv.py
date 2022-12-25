import csv
import io

from tiled_export.map.dataclasses import Tileset, TileLayer


def get_map_size(tiledmap):
    """Get total size of a map"""

    if not tiledmap.infinite:
        return (tiledmap.width, tiledmap.height)

    else:
        left = right = top = bottom = 0
        for layer in tiledmap.layers:
            for chunk in layer.chunks:
                if chunk.x < left:
                    left = chunk.x
                if chunk.x + chunk.width > right:
                    right = chunk.x + chunk.width
                if chunk.y < top:
                    top = chunk.y
                if chunk.y + chunk.height > bottom:
                    bottom = chunk.y + chunk.height

        return (right - left, bottom - top)


def get_map_origin_index(tiledmap):
    """Get index of map origin"""

    if not tiledmap.infinite:
        return (0, 0)

    else:
        x = y = 0

        for layer in tiledmap.layers:
            for chunk in layer.chunks:
                if chunk.x < x:
                    x = chunk.x
                if chunk.y < y:
                    y = chunk.y

        x = (-1) * x
        y = (-1) * y

        return (x, y)


def fix_gid(matrix, tilesets):
    """Fix the GIDs to make them comply with Tiled CSV export format"""

    # Get tile's tileset
    tileset = tilesets[0]
    for ts in tilesets:
        if ts.firstgid > tileset.firstgid and gid >= ts.firstgid:
            tileset = ts

    return gid - tileset.firstgid


class Table:

    def __init__(self, origin: tuple, size: tuple):

        self.origin = origin
        self.size = size
        self.array = [
            [
                -1
                for _ in range(size[0])
            ]
            for _ in range(size[1])
        ]

    def write(self, x, y, v):
        """Writes value v at coordinates (x, y)"""

        self.array[self.origin[1]+y][self.origin[0]+x] = v

    def get(self, x, y):
        """Gets value at coordinates (x, y)"""

        return self.array[self.origin[1]+y][self.origin[0]+x]

    def autocrop(self):
        """Crops a itself to leave no space around the map"""

        crop_left = self.size[0]
        crop_right = 0
        crop_top = self.size[1]
        crop_bottom = 0

        # For each tile
        for y, row in enumerate(self.array):
            for x, gid in enumerate(row):

                # If tile is not empty
                if gid != -1:

                    if x < crop_left:
                        crop_left = x

                    if x > crop_right:
                        crop_right = x

                    if y < crop_top:
                        crop_top = y

                    if y > crop_bottom:
                        crop_bottom = y

        # Crop
        self.array = self.array[crop_top:crop_bottom+1]
        for i in range(len(self.array)):
            self.array[i] = self.array[i][crop_left:crop_right+1]

    @staticmethod
    def from_tiledmap(tiledmap):

        # Get origin and size
        origin = get_map_origin_index(tiledmap)
        size = get_map_size(tiledmap)

        table = Table(origin, size)

        # Flatten layers' data into table
        for layer in tiledmap.layers:
            if isinstance(layer, TileLayer):
                if tiledmap.infinite:
                    for chunk, group in zip(layer.chunks, layer):
                        for y, row in enumerate(group):
                            for x, gid in enumerate(row):
                                if gid != 0:
                                    table.write(chunk.x+x, chunk.y+y, gid)
                else:
                    for group in layer:
                        for y, row in enumerate(group):
                            for x, gid in enumerate(row):
                                table.write(x, y, gid)

        return table

    def rows(self):
        return self.array


def export(tiledmap):
    """Exports a tiledmap to CSV"""

    table = Table.from_tiledmap(tiledmap)

    table.autocrop()

    out = io.StringIO()
    csv.writer(out).writerows(table.rows())

    return out.getvalue()
