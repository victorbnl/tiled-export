from abc import ABC

from pydantic_xml import BaseXmlModel, BaseGenericXmlModel, attr, element, wrapped

from typing import Optional, Type, Dict, List, Tuple, Literal
from pydantic import PositiveInt, NonNegativeInt

from tiled_export.types.root import RootNode
from tiled_export.types.point import Point


class Grid(BaseXmlModel, tag='grid'):

    orientation: Literal['unknown', 'orthogonal', 'isometric', 'staggered', 'horizontal'] = attr()

    width: NonNegativeInt = attr()
    height: NonNegativeInt = attr()



class TileOffset(BaseXmlModel, tag='tileoffset'):

    x: int = attr()
    y: int = attr()


class Tile(BaseXmlModel, tag='tile'):

    id_: Optional[int] = attr(name='id')

    image: Optional[str] = wrapped('image', attr(name='source'))
    imagewidth: Optional[int] = wrapped('image', attr(name='width'))
    imageheight: Optional[int] = wrapped('image', attr(name='height'))


class Tileset(ABC, BaseXmlModel):

    name: str = attr(default='')


class EmbeddedTileset(ABC, BaseXmlModel):

    firstgid: PositiveInt = attr()


class FullTileset(ABC, BaseXmlModel):

    class_: str = attr(default='')

    tilewidth: NonNegativeInt = attr()
    tileheight: NonNegativeInt = attr()

    spacing: NonNegativeInt = attr(default=0)
    margin: NonNegativeInt = attr(default=0)

    tilecount: NonNegativeInt = attr()
    columns: NonNegativeInt = attr()

    objectalignment: Literal['unspecified', 'topleft', 'top', 'topright', 'left', 'center', 'right', 'bottomleft', 'bottom', 'bottomright'] = attr(default='unspecified')
    tilerendersize: Literal['tile', 'grid'] = attr(default='tile')
    fillmode: Literal['stretch', 'preserve-aspect-fit'] = attr(default='stretch')

    tileoffset: TileOffset = element(tag='tileoffset', default=TileOffset(x=0, y=0))

    grid: Optional[Grid] = element(tag='grid')

    tiles: Optional[List[Tile]] = element(tag='tile')


class RootTileset(Tileset, RootNode, tag='tileset'):

    pass


class FullEmbeddedTileset(FullTileset, EmbeddedTileset, tag='tileset'):

    pass


class SourcedEmbeddedTileset(Tileset, EmbeddedTileset, tag='tileset'):

    source: Optional[str] = attr()
