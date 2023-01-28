"""
Map type definitions
"""


import lxml.etree as etree

from pydantic_xml import BaseXmlModel, attr, element
from pydantic import Field

from typing import Optional, Literal, List
from pydantic import NonNegativeInt

from tiled_export.types.base import Color
from tiled_export.types.tiled.root import RootNode
from tiled_export.types.tiled.tileset import EmbeddedTileset
from tiled_export.types.tiled.layer import Layer

from tiled_export.types import utils


class Map(BaseXmlModel, tag='map'):
    """
    A map
    """

    class_: str = attr(name='class', default='')

    orientation: Literal['unknown', 'orthogonal', 'isometric', 'staggered', 'horizontal'] = attr()
    renderorder: Literal['right-down', 'right-up', 'left-down', 'left-up'] = attr(default='right-down')

    width: NonNegativeInt = attr()
    height: NonNegativeInt = attr()

    tilewidth: NonNegativeInt = attr()
    tileheight: NonNegativeInt = attr()

    hexsidelength: Optional[int] = attr()

    staggeraxis: Optional[Literal['x', 'y']] = attr()
    staggerindex: Optional[Literal['even', 'odd']] = attr()

    backgroundcolor: Optional[Color] = attr()

    nextlayerid: Optional[NonNegativeInt] = attr()
    nextobjectid: Optional[NonNegativeInt] = attr()

    compressionlevel: int = attr(default=-1)
    infinite: bool = attr(default=False)

    tilesets: List[EmbeddedTileset] = Field(default_factory=list)

    layers: List[Layer] = Field(default_factory=list)

    @classmethod
    def from_xml_tree(cls, root: etree.Element) -> Optional[BaseXmlModel]:
        """
        Build object of type `cls` from XML node

        Overloaded to manually parse tilesets and layers

        Args:
            cls: Object type
            root: XML node to build the object from

        Returns:
            Object
        """

        obj = super().from_xml_tree(root)
        obj = utils.add_tilesets(cls, obj, root)
        obj = utils.add_layers(cls, obj, root)
        return obj


class RootMap(Map, RootNode, tag='map'):
    """
    A map when at root
    """

    pass
