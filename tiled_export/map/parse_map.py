from tiled_export.xml import Tree
from tiled_export.map.dataclasses import *


def parse_map(filename):
    """Parses XML map file into TiledMap object"""

    tree = Tree(filename)

    map_node = tree.child("map", prefix="/")
    map_attrs = map_node.attrs()

    tilesets = []
    for tileset_node in map_node.children("tileset"):

        tileset_attrs = tileset_node.attrs()

        tileset_attrs["filename"] = tileset_attrs["source"]
        del tileset_attrs["source"]

        tileset = Tileset(**tileset_attrs)
        tilesets.append(tileset)

    tile_layers = []
    for layer_node in map_node.children("layer"):

        layer_attrs = layer_node.attrs() | layer_node.child("data").attrs()

        args = {}

        if map_attrs["infinite"] == "1":

            chunks = []
            for chunk_node in layer_node.child("data").children("chunk"):

                chunk_attrs = chunk_node.attrs()
                chunk_data = chunk_node.text()

                chunk = Chunk(data=chunk_data, **chunk_attrs)
                chunks.append(chunk)

                args["chunks"] = chunks

        else:

            data_node = layer_node.child("data")
            data = data_node.text()

            args["data"] = data

        layer = TileLayer(**args, **layer_attrs)
        tile_layers.append(layer)

    object_groups = []
    for object_group_node in map_node.children("objectgroup"):

        object_group_attrs = object_group_node.attrs()

        objects = []
        for object_node in object_group_node.children("object"):

            object_attrs = object_node.attrs()

            object_ = Object(**object_attrs)
            objects.append(object_)

        object_group = ObjectGroup(objects=objects, **object_group_attrs)
        object_groups.append(object_group)

    layers = tile_layers + object_groups

    tiledmap = TiledMap(tilesets=tilesets, layers=layers, **map_attrs)
    return tiledmap
