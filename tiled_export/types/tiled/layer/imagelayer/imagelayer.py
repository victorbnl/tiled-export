from tiled_export.types.tiled.layer.layer import Layer

from typing import Optional
from pydantic import PositiveInt, conint, conlist
from tiled_export.types.qt import Color


class ImageLayer(Layer):

    id_: PositiveInt
    name: str = ""
    class_: Optional[str]

    repeatx: Optional[bool]
    repeaty: Optional[bool]

    format_: Optional[str]
    image: Optional[str]
    transparentcolor: Optional[Color]
