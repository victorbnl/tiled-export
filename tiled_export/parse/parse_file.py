from lxml import etree

from typing import Optional, Union

from tiled_export.types import RootMap, RootTileset


def parse_file(filename: str) -> Optional[Union[RootMap, RootTileset]]:
    """Parse file into a Tiled object"""

    # Get root node
    tree = etree.parse(filename)
    root = tree.getroot()
    roottag = root.tag

    # Parse it
    if roottag == 'map':
        return RootMap.from_xml_tree(root)
    elif roottag == 'tileset':
        return RootTileset.from_xml_tree(root)

    return None
