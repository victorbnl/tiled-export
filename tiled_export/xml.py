from lxml import etree


class Node:

    def __init__(self, node):
        """A XML node"""

        self.node = node

    def text(self):
        """Get node text"""

        return self.node.text.strip()

    def attrs(self):
        """Get attributes of node, adding an underscore to Python reserved keywords"""

        attrs = {}
        for k, v in self.node.attrib.items():

            if k in ("id", "class"):
                k += "_"

            attrs[k] = v

        return attrs

    def children(self, name, *, prefix="./"):
        """Gets list of children with given name"""

        return [Node(xnode) for xnode in self.node.xpath(prefix + name)]

    def child(self, name, *, prefix="./"):
        """Gets first child element with given name"""

        children = self.children(name, prefix=prefix)
        if len(children):
            return children[0]
        else:
            return None


class Tree(Node):

    def __init__(self, filename):
        """A XML tree"""

        node = etree.parse(filename)
        super().__init__(node)
