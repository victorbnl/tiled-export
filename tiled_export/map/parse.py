from lxml import etree

import csv
import base64
import gzip
import zlib
import zstd
import struct

from tiled_export.map.dataclasses import *


def parse_data(data, encoding="csv", compression=None, width=16, height=16):

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
        if compression == None:
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
        layer_attrs = get_attrs(node)

        # Get data format
        data_node = node.xpath("./data")[0]
        encoding = data_node.get("encoding")
        compression = data_node.get("compression")

        # Args to provide to TileLayer()
        args = {}

        # If map is infinite
        if (map_attrs["infinite"] == "1"):

            # Get chunks
            chunks = []
            for chunk_node in node.xpath("./data/chunk"):

                # Get chunk attributs
                chunk_attrs = get_attrs(chunk_node)

                # Parse chunk data
                width = int(chunk_node.get("width"))
                height = int(chunk_node.get("height"))
                parsed = parse_data(chunk_node.text, encoding, compression, width, height)

                chunk = Chunk(data=parsed, **chunk_attrs)
                chunks.append(chunk)

                args["chunks"] = chunks

        # If it is not
        else:

            # Get data
            data_node = node.xpath("./data")[0]
            width = int(map_node.get("width"))
            height = int(map_node.get("height"))
            data = parse_data(data_node.text, encoding, compression, width, height)

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
