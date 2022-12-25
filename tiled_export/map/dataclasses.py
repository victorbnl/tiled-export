import dataclasses
from dataclasses import dataclass, fields

from tiled_export.base_dataclass import Base


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

    data: list = None


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

    width: int = None
    height: int = None

    opacity: int = 1

    visible: bool = True

    x: int = 0
    y: int = 0

    chunks: list = None
    data: list = None

    def get_tiles(self):

        groups = []

        if self.chunks:
            for chunk in self.chunks:
                groups.append(chunk.data)

        if self.data:
            groups.append(self.data)

        return groups


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
