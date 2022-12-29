from dataclasses import dataclass, field

from tiled_export.types.tiled._base import *


@dataclass
class Wangset(BaseObject):

    name: str = ""

    type_: str = None
    tile: int = None

    colors: list = field(default_factory=list)
    wangtiles: list = field(default_factory=list)
