import unittest
import node


class TestNodes(unittest.TestCase):
    def test_leavesCount_noLeaves(self):
        cut = node.Nodes()
        self.assertEquals(0, cut.leavesCount())

    def test_leavesCount_3Leaves(self):
        cut = node.Nodes()

        mNode = node.Node(None)
        cut.nodesList.append(mNode)

        mNode = node.Node(None)
        cut.nodesList.append(mNode)

        mTmpNode = node.Node(mNode)
        mNode.nodesList.append(mTmpNode)

        mTmpNode = node.Node(mNode)
        mNode.nodesList.append(mTmpNode)

        self.assertEquals(3, cut.leavesCount())

if __name__ == '__main__':
    unittest.main()
