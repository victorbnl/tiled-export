from pydantic import BaseModel

from typing import Optional
from pydantic import PositiveInt, conint, conlist
from tiled_export.types.qt import Color


class ImageLayer(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: Optional[str]

    offsetx: Optional[int]
    offsety: Optional[int]

    parallaxx: Optional[int]
    parallaxy: Optional[int]

    x: int = 0
    y: int = 0

    opacity: conint(ge=0, le=1) = 1
    visible: bool = True
    tintcolor: Optional[Color]

    repeatx: Optional[bool]
    repeaty: Optional[bool]

    format_: Optional[str]
    image: Optional[str]
    transparentcolor: Optional[Color]
