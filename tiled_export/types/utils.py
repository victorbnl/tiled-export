"""
Methods for layer and tileset parsing
"""


from lxml import etree

from typing import Type, Dict, List
from pydantic_xml import BaseXmlModel

from tiled_export.types.tiled.layer import Layer
from tiled_export.types.tiled.tilelayer import TileLayer
from tiled_export.types.tiled.objectgroup import ObjectGroup
from tiled_export.types.tiled.imagelayer import ImageLayer
from tiled_export.types.tiled.tileset import Tileset, FullEmbeddedTileset, SourcedEmbeddedTileset

from tiled_export.types.tiled import group


def add_tilesets(cls, obj: BaseXmlModel, root: etree.Element) -> BaseXmlModel:
    """Return object with tilesets added"""

    tilesets: List[Tileset] = []
    for node in root.xpath('tileset'):
        if 'source' in node.attrib:
            tilesets.append(SourcedEmbeddedTileset.from_xml_tree(node))
        else:
            tilesets.append(FullEmbeddedTileset.from_xml_tree(node))

    return cls.parse_obj({**dict(obj), 'tilesets': tilesets})


def add_layers(cls, obj: BaseXmlModel, root: etree.Element) -> BaseXmlModel:
    """Return object with layers added"""

    layer_types: Dict[str, Type[Layer]] = {
        'layer': TileLayer,
        'objectgroup': ObjectGroup,
        'imagelayer': ImageLayer,
        'group': group.Group,
    }

    layers = []
    for node in root.xpath('|'.join(layer_types.keys())):
        layers.append(
            layer_types[node.tag].from_xml_tree(node)
        )

    return cls.parse_obj({**dict(obj), 'layers': layers})
