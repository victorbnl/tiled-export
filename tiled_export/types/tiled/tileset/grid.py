from dataclasses import dataclass

from tiled_export.types.tiled._base import *


@dataclass
class Grid(Base):

    orientation: str = None

    width: int = None
    height: int = None
