from pydantic import BaseModel

from typing import Literal
from pydantic import NonNegativeInt


class Grid(BaseModel):

    orientation: Literal["unknown", "orthogonal", "isometric", "staggered", "horizontal"]

    width: NonNegativeInt
    height: NonNegativeInt
