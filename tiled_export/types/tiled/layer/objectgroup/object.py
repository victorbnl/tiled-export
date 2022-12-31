from pydantic import BaseModel

from typing import Optional
from pydantic import PositiveInt, NonNegativeFloat


class Object(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    x: NonNegativeFloat = 0
    y: NonNegativeFloat = 0

    width: NonNegativeFloat = 0
    height: NonNegativeFloat = 0

    rotation: float = 0

    gid: Optional[int]

    visible: bool = True
