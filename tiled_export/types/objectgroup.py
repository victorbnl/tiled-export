from pydantic_xml import BaseXmlModel, attr

from typing import Optional, List, Literal
from pydantic import PositiveInt, NonNegativeFloat, NonNegativeInt

from tiled_export.types.layers import Layer


class Object(BaseXmlModel, tag='object'):

    id_: PositiveInt = attr(name='id')
    name: str = attr()
    class_: str = attr(name='class', default='')

    x: NonNegativeFloat = attr(default=0)
    y: NonNegativeFloat = attr(default=0)

    width: NonNegativeFloat = attr(default=0)
    height: NonNegativeFloat = attr(default=0)

    rotation: float = attr(default=0)

    gid: Optional[int] = attr()

    visible: bool = attr(default=True)


class ObjectGroup(Layer, tag='objectgroup'):

    id_: PositiveInt = attr(name='id')
    name: str = attr(default='')
    class_: str = attr(name='class', default='')

    color: Optional[str] = attr()

    width: Optional[NonNegativeInt] = attr()
    height: Optional[NonNegativeInt] = attr()

    draworder: Literal['index', 'topdown'] = attr(default='topdown')

    objects: List[Object]
