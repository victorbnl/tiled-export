from dataclasses import dataclass

from tiled_export.types.tiled._base import *


@dataclass
class ObjectGroup(Base):

    id_: int = None
    name: str = None

    opacity: int = 1

    visible: bool = True

    x: int = 0
    y: int = 0

    draworder: str = "topdown"

    objects: list = None
