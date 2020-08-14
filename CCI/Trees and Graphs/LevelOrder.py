"""
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Input: Given binary tree [3,9,20,null,null,15,7]
Output:
[
  [3],
  [9,20],
  [15,7]
]

"""

from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return []
    queue = deque([root])
    output = []
    while queue:
        current_level = []
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            current_level.append(node.val)
        output.append(current_level)
    return output

#[3,9,20,null,null,15,7]
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrder(root))
