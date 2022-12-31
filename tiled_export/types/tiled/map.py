from pydantic import BaseModel

from typing import Optional, Literal
from pydantic import NonNegativeInt
from tiled_export.types.qt import Color
from tiled_export.types.tiled.tileset import Tileset
from tiled_export.types.tiled.layer import TileLayer


class Map(BaseModel):

    version: str
    tiledversion: str

    orientation: Literal["unknown", "orthogonal", "isometric", "staggered", "horizontal"]
    renderorder: Literal["right-down", "right-up", "left-down", "left-up"] = "right-down"

    width: NonNegativeInt = 0
    height: NonNegativeInt = 0

    tilewidth: NonNegativeInt
    tileheight: NonNegativeInt

    hexsidelength: Optional[int]

    staggeraxis: Optional[Literal["x", "y"]]
    staggerindex: Optional[Literal["even", "odd"]]

    backgroundcolor: Color = None

    nextlayerid: Optional[NonNegativeInt]
    nextobjectid: Optional[NonNegativeInt]

    compressionlevel: int = -1
    infinite: bool

    properties: list = []
    tilesets: list[Tileset] = []
    layers: list[TileLayer] = []
