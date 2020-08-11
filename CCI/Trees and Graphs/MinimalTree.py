"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + ':L ' + "V:" + str(self.val) + " R:" + str(self.right) + ')'

class SortedArrayBST:

    def minimalTree(self, nums):
        if not nums: return None

        mid_point = len(nums)//2
        node = Node(nums[mid_point])
        node.left = self.minimalTree(nums[:mid_point])
        node.right = self.minimalTree(nums[mid_point+1:])
        return node

    def printTree(self,nums):
        return self.minimalTree(nums)





#nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
nums = [-10,-3,0,5,9]
Bst = SortedArrayBST()
print(Bst.minimalTree(nums))
