from dataclasses import dataclass, field

from tiled_export.types.tiled._base import *
from tiled_export.parse_data import parse_data


@dataclass
class TileLayer(BaseObject):

    id_: int = None
    name: str = None

    width: int = None
    height: int = None

    opacity: int = 1

    visible: bool = True

    x: int = 0
    y: int = 0

    offsetx: int = 0
    offsety: int = 0

    parallaxx: int = 1
    parallaxy: int = 1

    encoding: str = None
    compression: str = None

    chunks: list = field(default_factory=list)
    data: str = None

    def __iter__(self):

        groups = []

        if self.chunks:
            for chunk in self.chunks:
                groups.append(parse_data(chunk.data, self.encoding, self.compression, chunk.width, chunk.height))

        if self.data:
            groups.append(parse_data(self.data, self.encoding, self.compression, self.width, self.height))

        return groups.__iter__()
