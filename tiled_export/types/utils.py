from lxml import etree

from typing import Optional, Dict
from pydantic_xml import BaseXmlModel

from tiled_export.types.tilelayer import TileLayer
from tiled_export.types.objectgroup import ObjectGroup
from tiled_export.types.imagelayer import ImageLayer
from tiled_export.types.tileset import SourceTileset, FullTileset

from tiled_export.types import group


def add_tilesets(cls, obj: BaseXmlModel, root: etree.Element) -> Optional[BaseXmlModel]:
    """Return object with tilesets added"""

    if not obj:
        return None

    tilesets = []
    for node in root.xpath('tileset'):
        if 'source' in node.attrib:
            tilesets.append(SourceTileset.from_xml_tree(node))
        else:
            tilesets.append(FullTileset.from_xml_tree(node))

    return cls.parse_obj({**dict(obj), 'tilesets': tilesets})



def add_layers(cls, obj: BaseXmlModel, root: etree.Element) -> Optional[BaseXmlModel]:
    """Return object with layers added"""

    if not obj:
        return None

    layer_types = {
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
