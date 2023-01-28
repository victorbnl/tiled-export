from lxml import etree
from pydantic_xml import BaseXmlModel, attr

from typing import Optional, List
from pydantic import PositiveInt
from tiled_export.types.tiled.layer import Layer

from tiled_export.types import utils


class Group(Layer, tag='group'):
    """
    A layer group
    """

    id_: PositiveInt = attr(name='id')
    name: str = attr(default='')
    class_: str = attr(name='class', default='')

    layers: Optional[List[Layer]]

    @classmethod
    def from_xml_tree(cls, root: etree.Element) -> Optional['BaseXmlModel']:
        """
        Build object of type `cls` from XML node

        Overloaded to manually parse sublayers

        Args:
            cls: Object type
            root: XML node to build the object from

        Returns:
            Object
        """

        return utils.add_layers(cls, super().from_xml_tree(root), root)
