import lxml.etree as etree

from pydantic_xml import BaseXmlModel, attr, element
from pydantic import Field

from typing import Optional, Literal, List
from pydantic import NonNegativeInt

from tiled_export.types.root import RootNode
from tiled_export.types.color import Color
from tiled_export.types.tileset import Tileset
from tiled_export.types.layers import Layer

from tiled_export.types import utils


class Map(BaseXmlModel, tag='map'): # type: ignore[call-arg]

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

    tilesets: List[Tileset] = element(tag='tileset')

    layers: List[Layer] = Field(default_factory=list)

    @classmethod
    def from_xml_tree(cls, root: etree.Element) -> Optional[BaseXmlModel]:
        obj = super().from_xml_tree(root)
        obj = utils.add_tilesets(cls, obj, root)
        obj = utils.add_layers(cls, obj, root)
        return obj


class RootMap(Map, RootNode, tag='map'): # type: ignore[call-arg]
    pass
