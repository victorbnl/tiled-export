from tiled_export.types.tiled.layer.layer import Layer

from typing import Optional, Literal
from pydantic import PositiveInt, NonNegativeInt

from tiled_export.types.tiled.layer.tilelayer.chunk import Chunk


class TileLayer(Layer):

    id_: PositiveInt
    name: str = ""
    class_: str = ""

    width: NonNegativeInt
    height: NonNegativeInt

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
