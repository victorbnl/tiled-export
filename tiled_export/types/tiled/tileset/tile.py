from dataclasses import dataclass

from tiled_export.types.tiled._base import *


@dataclass
class Tile(Base):

    id_: int = None

    image: str = None

    imagewidth: int = None
    imageheight: int = None
