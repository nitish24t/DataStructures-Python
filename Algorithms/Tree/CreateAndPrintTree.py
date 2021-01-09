class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#                   10
#             7              20
#        5       9      15       30

class Tree:

    def getBinaryTree(self):
        self.root = Node(10)
        self.root.left = Node(7)
        self.root.right = Node(20)
        self.root.left.left = Node(5)
        self.root.left.right = Node(9)
        self.root.right.left = Node(15)
        self.root.right.right = Node(30)
        return self.root

    def preorderTraversalRecursive(self, root):
        if root:
            print(f"{root.data}", end=" ")
            self.preorderTraversalRecursive(root.left)
            self.preorderTraversalRecursive(root.right)

    def inorderTraversalRecursive(self, root):
        if root:
            self.inorderTraversalRecursive(root.left)
            print(f"{root.data}", end=" ")
            self.inorderTraversalRecursive(root.right)

    def postorderTraversalRecursive(self, root):
        if root:
            self.postorderTraversalRecursive(root.left)
            self.postorderTraversalRecursive(root.right)
            print(f"{root.data}", end=" ")



if __name__ == "__main__":
    print("hello world")
    T = Tree()
    root = T.getBinaryTree()
    print(str(root.data))

    print("Preorder Traversal")
    T.preorderTraversalRecursive(root)
    print("\n")
    print("Inorder Traversal")
    T.inorderTraversalRecursive(root)
    print("\n")
    print("Postorder Traversal")
    T.postorderTraversalRecursive(root)
    print("\n")




