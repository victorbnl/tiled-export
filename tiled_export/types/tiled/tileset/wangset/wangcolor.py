from dataclasses import dataclass

from tiled_export.types.tiled._base import *
from tiled_export.types.qt.color import Color


@dataclass
class WangColor(BaseObject):

    name: str = ""
    color: Color = None
    tile: int = None
    probability: int = None
