from pydantic import BaseModel

from typing import Optional, Literal
from pydantic import PositiveInt, NonNegativeInt, conint
from tiled_export.types import Color
from tiled_export.types.tiled.layer.objectgroup.object import Object


class ObjectGroup(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    color: Optional[Color]

    x: int = 0
    y: int = 0

    width: Optional[int]
    height: Optional[int]

    opacity: conint(ge=0, le=1)
    visible: bool = True
    tintcolor: Optional[Color]

    offsetx: Optional[NonNegativeInt] = 0
    offsety: Optional[NonNegativeInt] = 0

    parallaxx: Optional[NonNegativeInt] = 1
    parallaxy: Optional[NonNegativeInt] = 1

    draworder: Literal["index", "topdown"] = "topdown"

    # properties
    objects: list[Object] = []
