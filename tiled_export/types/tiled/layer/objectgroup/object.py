from pydantic import BaseModel

from typing import Optional
from pydantic import PositiveInt


class Object(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    x: float = 0
    y: float = 0

    width: float = 0
    height: float = 0

    rotation: int = 0

    gid: Optional[int]

    visible: bool = True
