from lxml import etree

from tiled_export.types import RootMap, RootTileset


def parse_file(filename):
    """Parse file into a Tiled object"""

    tree = etree.parse(filename)
    root = tree.getroot()
    roottag = root.tag

    if roottag == 'map':
        return RootMap.from_xml_tree(root)
    elif roottag == 'tileset':
        return RootTileset.from_xml_tree(root)
