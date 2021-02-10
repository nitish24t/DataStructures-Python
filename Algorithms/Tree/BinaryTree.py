import CreateAndPrintTree as BT

class BinaryTree:

    def getHeightRecursive(self,root):
        if root is None:
            return -1
        return 1 + max(self.getHeightRecursive(root.left),self.getHeightRecursive(root.right))


T = BT.Tree()
root = T.getBinaryTree()

BTree = BinaryTree()
height = BTree.getHeightRecursive(root)
print(height)