from lxml import etree

from typing import Optional
from pydantic_xml import BaseXmlModel

from tiled_export.types import RootMap, RootTileset


def parse_file(filename: str) -> Optional[BaseXmlModel]:
    """Parse file into a Tiled object"""

    # Get root node
    tree = etree.parse(filename)
    root = tree.getroot().getroottree().getroot()
    roottag = root.tag

    # Parse it
    if roottag == 'map':
        return RootMap.from_xml_tree(root)
    elif roottag == 'tileset':
        return RootTileset.from_xml_tree(root) # type: ignore[arg-type]

    return None
