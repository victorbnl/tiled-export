from pydantic import BaseModel

from tiled_export.types.qt import Color


class WangColor(BaseModel):

    name: str
    class_: str = ""
    color: Color
    tile: int
    probability: int = 0
