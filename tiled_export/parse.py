from tiled_export.xml import Tree
from tiled_export.types import *


def parse(filename):
    """Parse a Tiled XML file"""

    tree = Tree(filename)

    return parse_node(tree.root())


def parse_node(node):
    """Parse a Tiled XML node"""

    # Node is a map
    if node.tag() == "map":

        # Get attributes
        attrs = node.attrs()

        tiledmap = Map(**attrs)

        # Parse children
        for child_node in node.children():
            child = parse_node(child_node)

            # Child is tileset
            if isinstance(child, Tileset):
                tiledmap.tilesets.append(child)

            # Child is layer
            if isinstance(child, TileLayer):
                tiledmap.layers.append(child)

        return tiledmap

    # Node is a tileset
    if node.tag() == "tileset":

        # Get attributes
        attrs = node.attrs()
        if "source" in attrs.keys():
            attrs["filename"] = attrs["source"]
            del attrs["source"]

        tileset = Tileset(**attrs)

        # Parse children
        for child_node in node.children():
            child = parse_node(child_node)

            # Child is grid
            if isinstance(child, Grid):
                tileset.grid = child

            # Child is tile
            if isinstance(child, Tile):
                tileset.tiles.append(child)

            # Child is wangset list
            if isinstance(child, list):
                if isinstance(child[0], Wangset):
                    tileset.wangsets = child

        return tileset

    # Node is a tileset grid
    if node.tag() == "grid":

        return Grid(**node.attrs())

    # Node is a tileset tile
    if node.tag() == "tile":

        attrs = node.attrs()

        # Get image attributes
        img_attrs = node.child().attrs()
        attrs["image"] = img_attrs["source"]
        attrs["imagewidth"] = img_attrs["width"]
        attrs["imageheight"] = img_attrs["height"]

        tile = Tile(**attrs)

        return tile

    # Node is a tileset wangset list
    if node.tag() == "wangsets":

        wangsets = []

        for child_node in node.children():
            child = parse_node(child_node)

            if isinstance(child, Wangset):
                wangsets.append(child)

        return wangsets

    # Node is a tileset wangset
    if node.tag() == "wangset":

        wangset = Wangset(**node.attrs())

        for child_node in node.children():
            child = parse_node(child_node)

            # Child is a wangcolor
            if isinstance(child, WangColor):
                wangset.colors.append(child)

        return wangset

    # Node is a tileset wangset wangcolor
    if node.tag() == "wangcolor":

        attrs = node.attrs()

        # Get color
        color = Color(attrs["color"])
        attrs["color"] = color

        return WangColor(**attrs)

    # Node is a tile layer
    if node.tag() == "layer":

        # Get data node
        data_node = node.child()

        # Gather data attributes and layer attributes
        attrs = node.attrs() | data_node.attrs()

        layer = TileLayer(**attrs)

        # Get data
        layer.data = data_node.text() or None
        # For data children (supposedly none or chunks)
        for child_node in data_node.children():
            child = parse_node(child_node)
            if isinstance(child, Chunk):
                layer.chunks.append(child)

        return layer

    # Node is a tile layer data chunk
    if node.tag() == "chunk":
        return Chunk(data=node.text(), **node.attrs())