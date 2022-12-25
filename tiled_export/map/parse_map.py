from lxml import etree

from tiled_export.map.dataclasses import *


def get_attrs(node):

    attrs = {}
    for k, v in node.attrib.items():
        if k in ("id", "class"):
            k += "_"
        attrs[k] = v

    return attrs


def parse_map(filename):

    tree = etree.parse(filename)

    map_node = tree.xpath("/map")[0]

    # Map attributes
    map_attrs = get_attrs(map_node)

    # Get tilesets
    tilesets = []
    for node in map_node.xpath("./tileset"):

        # Tileset attributes
        tileset_attrs = get_attrs(node)

        tileset = Tileset(**tileset_attrs)
        tilesets.append(tileset)

    # Get tile layers
    tile_layers = []
    for node in map_node.xpath("./layer"):

        # Layer attributes
        layer_attrs = get_attrs(node) | get_attrs(node.xpath("./data")[0])

        # Args to provide to TileLayer()
        args = {}

        # If map is infinite
        if (map_attrs["infinite"] == "1"):

            # Get chunks
            chunks = []
            for chunk_node in node.xpath("./data/chunk"):

                # Get chunk attributes
                chunk_attrs = get_attrs(chunk_node)

                # Parse chunk data
                data = chunk_node.text.strip()

                chunk = Chunk(data=data, **chunk_attrs)
                chunks.append(chunk)

                args["chunks"] = chunks

        # If it is not
        else:

            # Get data
            data_node = node.xpath("./data")[0]
            data = data_node.text.strip()

            args["data"] = data

        layer = TileLayer(
            **args,
            **layer_attrs
        )
        tile_layers.append(layer)

    # Get object groups
    object_groups = []
    for node in map_node.xpath("./objectgroup"):

        # Group attributes
        object_group_attrs = get_attrs(node)

        # Get objects
        objects = []
        for obj_node in node.xpath("./object"):

            # Object attributes
            object_attrs = get_attrs(obj_node)

            obj = Object(**object_attrs)
            objects.append(obj)

        object_group = ObjectGroup(
            objects=objects,
            **object_group_attrs
        )
        object_groups.append(object_group)

    layers = tile_layers + object_groups

    tilemap = TiledMap(
        tilesets=tilesets,
        layers=layers,
        **map_attrs
    )

    return tilemap
