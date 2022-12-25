from lxml import etree

from tiled_export.tileset.dataclasses import *


def get_attrs(node):

    attrs = {}
    for k, v in node.attrib.items():
        if k in ("id", "class"):
            k += "_"
        attrs[k] = v

    return attrs


def parse_tileset(filename):

    tree = etree.parse(filename)

    tileset_node = tree.xpath("/tileset")[0]
    tileset_attrs = get_attrs(tileset_node)

    grid_node = tileset_node.xpath("./grid")[0]
    grid_attrs = get_attrs(grid_node)
    grid = Grid(**grid_attrs)

    tiles = []
    for tile_node in tileset_node.xpath("./tile"):

        tile_attrs = get_attrs(tile_node)

        img_node = tile_node.xpath("./image")[0]
        img_attrs = get_attrs(img_node)

        tile_attrs["image"] = img_attrs["source"]
        tile_attrs["imagewidth"] = img_attrs["width"]
        tile_attrs["imageheight"] = img_attrs["height"]

        tile = Tile(**tile_attrs)
        tiles.append(tile)

    tileset = Tileset(tiles=tiles, grid=grid, **tileset_attrs)
    return tileset


if __name__ == "__main__":

    print(parse_tileset("ad.tsx"))
