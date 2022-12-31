from pydantic import BaseModel


class WangTile(BaseModel):

    tileid: int
    wangid: str
