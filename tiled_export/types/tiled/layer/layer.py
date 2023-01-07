from pydantic import BaseModel

from typing import Optional
from pydantic import conint
from tiled_export.types.qt import Color


class Layer(BaseModel):

    x: int = 0
    y: int = 0

    offsetx: int = 0
    offsety: int = 0

    parallaxx: int = 1
    parallaxy: int = 1

    opacity: conint(ge=0, le=1) = 1
    visible: bool = True
    tintcolor: Optional[Color]
