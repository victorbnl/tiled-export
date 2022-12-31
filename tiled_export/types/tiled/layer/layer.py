from pydantic import BaseModel

from typing import Optional
from pydantic import conint
from tiled_export.types.qt import Color


class Layer(BaseModel):

    x: int = 0
    y: int = 0

    offsetx: Optional[int]
    offsety: Optional[int]

    parallaxx: Optional[int]
    parallaxy: Optional[int]

    opacity: conint(ge=0, le=1) = 1
    visible: bool = True
    tintcolor: Optional[Color]
