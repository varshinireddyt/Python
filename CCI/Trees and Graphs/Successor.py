"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each node has a link to its parent.
"""

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
#insert
def insert(node, data):

    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left,data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right,data)
            node.right = temp
            temp.parent = node
        return node
#min value in a subtree
def minValue(node):
    current = node
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current
#finding succesor by inorder traversal
def inOrderSuccessor(root, node):
    #if right is not None then min value in right subtree
    if node.right is not None:
        return minValue(node.right)
    # else ancesotor parent is left child of root node
    p = node.parent
    while p is not None:
        if node != p.right:
            break
        node = p
        p = p.parent
    return p


root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root,4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)

find = root.left.right.right

successor = inOrderSuccessor(root,find)
if successor is not None:
    print(' % d Successor is % d '  %(find.data,successor.data ))

else:
    print('No Successor')

