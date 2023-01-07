from tiled_export.types.tiled.layer.layer import Layer

from typing import Optional, List
from pydantic import PositiveInt


class Group(Layer):

    id_: PositiveInt
    name: str = ""
    class_: Optional[str]

    layers: Optional[List[Layer]]
