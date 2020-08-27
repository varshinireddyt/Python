"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.

Condition: leftchild < root < rightchild
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def validateBST(root):
    return checkBST(root, None, None)

def checkBST(root, minVal, maxVal):
    if root is None:
        return True

    if (minVal != None and root.val <= minVal) or (maxVal != None and root.val >= maxVal):
        return False
    if not checkBST(root.left, minVal, root.val) or not checkBST(root.right, root.val, maxVal):
        return False

    return True


root = Node(8)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(6)
# root.right.left = Node(9)
root.right.right = Node(20)


print(checkBST(root,None,None))





