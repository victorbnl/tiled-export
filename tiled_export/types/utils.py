from lxml import etree

from typing import Optional, Type, Dict, List
from pydantic_xml import BaseXmlModel

from tiled_export.types.layers import Layer
from tiled_export.types.tilelayer import TileLayer
from tiled_export.types.objectgroup import ObjectGroup
from tiled_export.types.imagelayer import ImageLayer
from tiled_export.types.tileset import Tileset, FullEmbeddedTileset, SourcedEmbeddedTileset

from tiled_export.types import group


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
