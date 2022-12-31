from pydantic import BaseModel

from typing import Optional
from pydantic import PositiveInt, conint, conlist
from tiled_export.types.qt import Color


class ImageLayer(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    offsetx: int = 0
    offsety: int = 0

    parallaxx: int = 1
    parallaxy: int = 1

    x: int = 0
    y: int = 0

    opacity: conint(ge=0, le=1) = 1
    visible: bool = True
    tintcolor: Optional[Color]

    repeatx: bool = False
    repeaty: bool = False

    format_: Optional[str]
    source: Optional[str]
    transparentcolor: Optional[Color]
