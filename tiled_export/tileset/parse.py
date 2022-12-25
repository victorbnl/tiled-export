from tiled_export.xml import Tree
from tiled_export.tileset.dataclasses import *


def parse_tileset(filename):
    """Parses XML tileset into Tileset object"""

    tree = Tree(filename)

    tileset_node = tree.child("tileset", prefix="/")
    tileset_attrs = tileset_node.attrs()

    grid_node = tileset_node.child("grid")
    grid_attrs = grid_node.attrs()
    grid = Grid(**grid_attrs)

    tiles = []
    for tile_node in tileset_node.children("tile"):

        tile_attrs = tile_node.attrs()

        image_node = tile_node.child("image")
        image_attrs = image_node.attrs()

        tile_attrs["image"] = image_attrs["source"]
        tile_attrs["imagewidth"] = image_attrs["width"]
        tile_attrs["imageheight"] = image_attrs["height"]

        tile = Tile(**tile_attrs)
        tiles.append(tile)

    tileset = Tileset(tiles=tiles, grid=grid, **tileset_attrs)
    return tileset
