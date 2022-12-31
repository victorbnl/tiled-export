from tiled_export.types.tiled.layer.layer import Layer

from typing import Optional, Union
from pydantic import PositiveInt, conint
from tiled_export.types.qt import Color


class Group(Layer):

    id_: PositiveInt
    name: str = ""
    class_: Optional[str]

    layers: Optional[list[Layer]]
