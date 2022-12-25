import dataclasses
from dataclasses import dataclass, fields

from tiled_export.base_dataclass import Base
from tiled_export.map.parse_data import parse_data


@dataclass
class Tileset(Base):

    firstgid: int = None
    source: str = None


@dataclass
class Chunk(Base):

    width: int = None
    height: int = None

    x: int = None
    y: int = None

    data: str = None


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


@dataclass
class TileLayer(Base):

    id_: int = None
    name: str = None
    class_: str = ""

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

    chunks: list = None
    data: str = None

    def __iter__(self):

        groups = []

        if self.chunks:
            for chunk in self.chunks:
                groups.append(parse_data(chunk.data, self.encoding, self.compression, chunk.width, chunk.height))

        if self.data:
            groups.append(parse_data(self.data, self.encoding, self.compression, self.width, self.height))

        return groups.__iter__()


@dataclass
class ObjectGroup(Base):

    id_: int = None
    name: str = None

    opacity: int = 1

    visible: bool = True

    x: int = 0
    y: int = 0

    draworder: str = "topdown"

    objects: list = None


@dataclass
class TiledMap(Base):

    version: str = None
    tiledversion: str = None

    orientation: str = None
    renderorder: str = None
    compressionlevel: int = -1
    infinite: bool = None
    backgroundcolor: str = None

    nextlayerid: int = None
    nextobjectid: int = None

    width: int = None
    height: int = None

    tilewidth: int = None
    tileheight: int = None

    tilesets: list = None

    layers: list = None
