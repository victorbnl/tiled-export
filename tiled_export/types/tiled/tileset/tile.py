from pydantic import BaseModel

from typing import Optional


class Tile(BaseModel):

    id_: Optional[int]

    image: Optional[str]

    imagewidth: Optional[int]
    imageheight: Optional[int]
