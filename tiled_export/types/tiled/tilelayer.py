"""
Tile layer type definitions
"""


from pydantic_xml import BaseXmlModel, attr, element, wrapped

from typing import Optional, List, Literal
from pydantic import PositiveInt, NonNegativeInt, constr

from tiled_export.types.tiled.layer import Layer

from tiled_export.parse import parse_data


class Chunk(BaseXmlModel, tag='chunk'):
    """
    A data chunk
    """

    x: int = attr()
    y: int = attr()

    width: NonNegativeInt = attr()
    height: NonNegativeInt = attr()

    data: constr(strip_whitespace=True)


class TileLayer(Layer, tag='layer'):
    """
    A tile layer
    """

    id_: PositiveInt = attr(name='id')
    name: str = attr(default='')
    class_: str = attr(name='class', default='')

    width: NonNegativeInt = attr()
    height: NonNegativeInt = attr()

    encoding: Literal['csv', 'base64'] = wrapped('data', attr())
    compression: Literal['', 'gzip', 'zlib', 'zstd'] = wrapped('data', attr(default=''))

    data: Optional[constr(strip_whitespace=True)] = element(tag='data')

    chunks: Optional[List[Chunk]] = wrapped('data', element(tag='chunk'))
