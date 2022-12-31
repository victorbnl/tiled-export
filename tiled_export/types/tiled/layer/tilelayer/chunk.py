from pydantic import BaseModel


class Chunk(BaseModel):

    x: int
    y: int

    width: int
    height: int

    data: str
