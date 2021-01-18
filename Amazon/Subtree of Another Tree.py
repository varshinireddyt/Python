"""Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself. """
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, s, t):
        if not t:
            return True
        if not s:
            return False

        def isSame(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

        def find(s, t):
            if not s and not t:
                return True
            elif not s or not t:
                return False
            if isSame(s, t):
                return True
            return find(s.left, t) or find(s.right, t)

        return find(s, t)
