"""
Tileset type definitions
"""

from abc import ABC

from pydantic_xml import BaseXmlModel, BaseGenericXmlModel, attr, element, wrapped

from typing import Optional, Type, Dict, List, Tuple, Literal
from pydantic import PositiveInt, NonNegativeInt

from tiled_export.types.tiled.root import RootNode
from tiled_export.types.base import Point


class Grid(BaseXmlModel, tag='grid'):
    """
    A tileset grid
    """

    orientation: Literal['unknown', 'orthogonal', 'isometric', 'staggered', 'horizontal'] = attr()

    width: NonNegativeInt = attr()
    height: NonNegativeInt = attr()


class TileOffset(BaseXmlModel, tag='tileoffset'):
    """
    A tileset offset
    """

    x: int = attr()
    y: int = attr()


class Tile(BaseXmlModel, tag='tile'):
    """
    A tileset tile
    """

    id_: Optional[int] = attr(name='id')

    image: Optional[str] = wrapped('image', attr(name='source'))
    imagewidth: Optional[int] = wrapped('image', attr(name='width'))
    imageheight: Optional[int] = wrapped('image', attr(name='height'))


class Tileset(BaseXmlModel):
    """
    A tileset
    """

    name: str = attr(default='')


class EmbeddedTileset(Tileset):
    """
    An embedded tileset
    """

    firstgid: PositiveInt = attr()


class FullTileset(Tileset):
    """
    A full tileset (as opposed to sourced)
    """

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


class RootTileset(FullTileset, RootNode, tag='tileset'):
    """
    A tileset when at root
    """

    pass


class FullEmbeddedTileset(FullTileset, EmbeddedTileset, tag='tileset'):
    """
    A full and embedded tileset
    """

    pass


class SourcedEmbeddedTileset(EmbeddedTileset, tag='tileset'):
    """
    A sourced tileset
    """

    source: Optional[str] = attr()
