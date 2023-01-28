"""
Layer type definitions
"""


from pydantic_xml import BaseXmlModel, attr

from typing import Optional
from pydantic import conint


class Layer(BaseXmlModel):
    """
    A map layer
    """

    x: int = attr(default=0)
    y: int = attr(default=0)

    offsetx: float = attr(default=0)
    offsety: float = attr(default=0)

    parallaxx: int = attr(default=1)
    parallaxy: int = attr(default=1)

    opacity: conint(ge=0, le=1) = attr(default=1)
    visible: bool = attr(default=True)
    tintcolor: Optional[str] = attr()
