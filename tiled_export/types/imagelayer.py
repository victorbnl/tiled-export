from pydantic_xml import attr, wrapped

from typing import Optional
from pydantic import PositiveInt, NonNegativeInt

from tiled_export.types.layers import Layer


class ImageLayer(Layer, tag='imagelayer'):

    id_: PositiveInt = attr(name='id')
    name: str = attr(default='')
    class_: str = attr(name='class', default='')

    width: NonNegativeInt = wrapped('image', attr())
    height: NonNegativeInt = wrapped('image', attr())

    repeatx: Optional[bool] = attr()
    repeaty: Optional[bool] = attr()

    format_: Optional[str] = wrapped('image', attr(name='format'))
    image: Optional[str] = wrapped('image', attr(name='source'))
    transparentcolor: Optional[str] = wrapped('image', attr(name='trans'))
