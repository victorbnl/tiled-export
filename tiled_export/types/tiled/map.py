from dataclasses import dataclass, field

from tiled_export.types.tiled._base import *
from tiled_export.types.qt.color import Color


@dataclass
class Map(BaseObject):

    version: str = None
    tiledversion: str = None

    orientation: str = None
    renderorder: str = None
    compressionlevel: int = -1
    infinite: bool = None
    backgroundcolor: Color = None

    nextlayerid: int = None
    nextobjectid: int = None

    width: int = None
    height: int = None

    tilewidth: int = None
    tileheight: int = None

    tilesets: list = field(default_factory=list)

    layers: list = field(default_factory=list)
