from pydantic import BaseModel

from typing import Optional
from pydantic import conlist
from tiled_export.types.tiled.tileset.wangset.wangcolor import WangColor


class Wangset(BaseModel):

    name: str
    class_: str = ""

    type_: Optional[int]
    tile: int

    colors: conlist(WangColor, max_items=255)
    wangtiles: list = []
