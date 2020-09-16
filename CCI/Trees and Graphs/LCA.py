"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary
tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

Leetcode 236

Solution:

if root founds one of the key then root
if one key is in left subtree and another in right subtree then root
if both keys are in left subtree then one of the left subtree else right subtree
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root,p,q):

    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    leftSubTree = lowestCommonAncestor(root.left,p,q)
    rightSubTree = lowestCommonAncestor(root.right,p,q)

    if leftSubTree and rightSubTree:
        return root

    if leftSubTree is not None:
        return leftSubTree
    else:
        return rightSubTree



root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.left.left = Node(None)
root.left.left.right = Node(None)
root.left.right.left = Node(7)
root.left.right.right = Node(4)


print('LCA: ', lowestCommonAncestor(root,5,1).val)