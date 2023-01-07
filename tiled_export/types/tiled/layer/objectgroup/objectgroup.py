from tiled_export.types.tiled.layer.layer import Layer

from typing import Optional, List, Literal
from pydantic import PositiveInt, NonNegativeInt
from tiled_export.types import Color
from tiled_export.types.tiled.layer.objectgroup.object import Object


class ObjectGroup(Layer):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    color: Optional[Color]

    width: Optional[NonNegativeInt]
    height: Optional[NonNegativeInt]

    draworder: Literal["index", "topdown"] = "topdown"

    # properties
    objects: List[Object] = []
