from pydantic import BaseModel

from typing import Optional, Literal
from pydantic import PositiveInt, NonNegativeInt
from tiled_export.types.qt import Point
from tiled_export.types.tiled.tileset.grid import Grid
from tiled_export.types.tiled.tileset.tile import Tile
from tiled_export.types.tiled.tileset.wangset import Wangset


class Tileset(BaseModel):

    name: str = ""

    firstgid: PositiveInt
    filename: Optional[str]

    tilewidth: Optional[NonNegativeInt]
    tileheight: Optional[NonNegativeInt]

    spacing: Optional[NonNegativeInt]
    margin: Optional[NonNegativeInt]

    tilecount: Optional[NonNegativeInt]

    columns: Optional[NonNegativeInt]

    objectalignment: Optional[Literal["unspecified", "topleft", "top", "topright", "left", "center", "right", "bottomleft", "bottom", "bottomright"]] = "unspecified"
    tilerendersize: Optional[Literal["tile", "grid"]] = "tile"
    fillmode: Optional[Literal["stretch", "preserve-aspect-fit"]] = "stretch"

    tileoffset: Optional[Point]

    grid: Optional[Grid]

    tiles: Optional[list[Tile]]
    wangsets: Optional[list[Wangset]]
