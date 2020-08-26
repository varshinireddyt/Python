"""
Check Balanced: Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree such that
the heights of the two subtrees of any node never differ by more than one.


Conditions: Height(left child -right child) <= 1
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.height = 0


def checkBalanced(root, height):

    leftHeight = Height()
    rightHeight = Height()

    if root is None:
        return True
    l = checkBalanced(root.left,leftHeight)
    r = checkBalanced(root.right, rightHeight)

    height.height = max(leftHeight.height,rightHeight.height) + 1

    if abs(leftHeight.height - rightHeight.height) <= 1:   
        return  l and r

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

height = Height()

if checkBalanced(root, height):
    print('Balanced')
else:
    print('Not Balanced')

