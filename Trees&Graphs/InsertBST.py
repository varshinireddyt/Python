"""
Leetcode 701: Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5
"""
# Time complexity: O(N)

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root,val):
        if root is None:
            return TreeNode(val)
        else:
             if root.val < val:
                 root.right = self.insertIntoBST(root.right,val)
             else:
                 root.left = self.insertIntoBST(root.left,val)
        return root

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    def printPreorder(self,root):
        if root:
            print(root.val)
            self.printPreorder(root.left)
            self.printPreorder(root.right)


root = TreeNode(4)
insert = Solution()
root = insert.insertIntoBST(root,2)
root = insert.insertIntoBST(root,7)
root = insert.insertIntoBST(root,1)
root = insert.insertIntoBST(root,3)
root = insert.insertIntoBST(root,5)
sol = Solution()
sol.printPreorder(root)







