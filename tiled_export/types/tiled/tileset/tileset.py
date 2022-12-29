from dataclasses import dataclass, field

from tiled_export.types.tiled._base import *
from tiled_export.types.qt import Point
from tiled_export.types.tiled.tileset.grid import Grid


@dataclass
class Tileset(BaseObject):

    name: str = ""

    version: str = None
    tiledversion: str = None

    firstgid: int = None
    filename: str = None

    tilewidth: int = None
    tileheight: int = None

    tilecount: int = None

    spacing: int = 0
    margin: int = 0
    columns: int = 0

    objectalignment: str = "unspecified"
    tilerendersize: str = "tile"
    fillmode: str = "stretch"

    tileoffset: Point = Point()

    grid: Grid = None

    tiles: list = field(default_factory=list)

    wangsets: list = field(default_factory=list)
