from dataclasses import dataclass

from tiled_export.types.tiled._base import *


@dataclass
class Chunk(Base):

    x: int = None
    y: int = None

    width: int = None
    height: int = None

    data: str = None
