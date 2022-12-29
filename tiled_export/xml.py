import xml.etree.cElementTree as etree


class Node:

    def __init__(self, node):
        """A XML node"""

        self.node = node

    def tag(self):
        """Gets node tag"""

        return self.node.tag

    def text(self):
        """Gets node text"""

        return self.node.text.strip()

    def attrs(self):
        """Gets attributes of node, adding an underscore to Python reserved keywords"""

        attrs = {}
        for k, v in self.node.attrib.items():

            if k in ("id", "class", "type"):
                k += "_"

            attrs[k] = v

        return attrs

    def children(self):
        """Gets list of children"""

        return [Node(xnode) for xnode in self.node]

    def child(self):
        """Gets first child element"""

        children = self.children()
        if len(children):
            return children[0]
        else:
            return None


class Tree():

    def __init__(self, filename):
        """A XML tree"""

        self.tree = etree.parse(filename)

    def root(self):
        """Get tree's root node"""

        return Node(self.tree.getroot())
