class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrder(root):
    if root is None:
        return None
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)


def inOrder(root):
    if root is None:
        return None
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)


tree = Node(1)
tree2 = Node(2)
tree3 = Node(3)
tree4 = Node(4)
tree5 = Node(5)
tree6 = Node(6)
tree7 = Node(7)

tree5.left = tree6
tree5.right = tree7
tree4.left = tree5
tree3.right = tree4

tree.left = tree2
tree.right = tree3



#preOrder(tree)
inOrder(tree)