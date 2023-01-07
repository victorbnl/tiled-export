from pydantic import BaseModel

from typing import Optional, List, Literal
from pydantic import PositiveInt, NonNegativeInt
from tiled_export.types.qt import Point
from tiled_export.types.tiled.tileset.grid import Grid
from tiled_export.types.tiled.tileset.tile import Tile
from tiled_export.types.tiled.tileset.wangset import Wangset


class Tileset(BaseModel):
    pass


class SourceTileset(Tileset):

    name: str = ""
    firstgid: PositiveInt
    source: str


class FullTileset(BaseModel):

    version: str
    tiledversion: str

    name: str = ""
    class_: str = ""

    tilewidth: NonNegativeInt
    tileheight: NonNegativeInt

    spacing: NonNegativeInt = 0
    margin: NonNegativeInt = 0

    tilecount: NonNegativeInt

    columns: NonNegativeInt

    objectalignment: Literal["unspecified", "topleft", "top", "topright", "left", "center", "right", "bottomleft", "bottom", "bottomright"] = "unspecified"
    tilerendersize: Literal["tile", "grid"] = "tile"
    fillmode: Literal["stretch", "preserve-aspect-fit"] = "stretch"

    tileoffset: Point = Point(x=0, y=0)

    grid: Optional[Grid]

    tiles: Optional[List[Tile]]
    wangsets: Optional[List[Wangset]]
