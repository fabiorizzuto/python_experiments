class Node:
    def __init__(self, parent):
        if not parent is None:
            assert isinstance(parent, Node)
            self.parent = parent
        else:
            self.parent = None

        self.nodesList = []
        self.data = None


class Nodes:
    """Nodes class is intended to be the root of the tree"""
    def __init__(self):
        self.nodesList = []

    def _getLeavesCount(self, node):
        if node is None:
            return 0
        elif len(node.nodesList) == 0:
            return 1
        else:
            count = 0
            for item in node.nodesList:
                count = count + self._getLeavesCount(item)
            return count

    def leavesCount(self):
        """Counts the leaves of the tree. Leaves are nodes without childen"""
        if len(self.nodesList) > 0:
            return self._getLeavesCount(self)
        else:
            return 0