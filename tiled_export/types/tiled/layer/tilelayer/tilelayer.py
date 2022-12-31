from pydantic import BaseModel

from typing import Optional, Literal
from pydantic import PositiveInt, conint
from pydantic.color import Color

from tiled_export.types.tiled.layer.tilelayer.chunk import Chunk


class TileLayer(BaseModel):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    x: int = 0
    y: int = 0

    width: int
    height: int

    opacity: conint(ge=0, le=1) = 1
    visible: bool = True

    tintcolor: Optional[Color]

    offsetx: int = 0
    offsety: int = 0

    parallaxx: int = 1
    parallaxy: int = 1

    encoding: Optional[Literal["csv", "base64"]]
    compression: Optional[Literal["uncompressed", "gzip", "zlib", "zstd"]]

    chunks: Optional[list[Chunk]]
    data: Optional[str]

    # def __iter__(self):

    #     groups = []

    #     if self.chunks:
    #         for chunk in self.chunks:
    #             groups.append(parse_data(chunk.data, self.encoding, self.compression, chunk.width, chunk.height))

    #     if self.data:
    #         groups.append(parse_data(self.data, self.encoding, self.compression, self.width, self.height))

    #     return groups.__iter__()
