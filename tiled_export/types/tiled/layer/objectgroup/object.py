from dataclasses import dataclass

from tiled_export.types.tiled._base import *


@dataclass
class Object(Base):

    id_: int = None
    name: str = ""
    class_: str = ""

    x: float = None
    y: float = None

    width: float = None
    height: float = None

    rotation: int = 0

    visible: bool = True
