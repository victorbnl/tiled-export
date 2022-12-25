from dataclasses import dataclass

from tiled_export.base_dataclass import Base


@dataclass
class Grid(Base):

    orientation: str = None

    width: int = None
    height: int = None


@dataclass
class Tile(Base):

    id_: int = None

    image: str = None

    imagewidth: int = None
    imageheight: int = None


@dataclass
class Tileset(Base):

    version: str = None
    tiledversion: str = None

    name: str = None

    tilewidth: int = None
    tileheight: int = None

    tilecount: int = None

    columns: int = 0

    grid: Grid = None

    tiles: list = None
