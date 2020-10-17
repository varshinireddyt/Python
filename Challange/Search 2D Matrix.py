"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Input: matrix = [], target = 0
Output: false
"""

class Solution:
    def searchMatrix(self, matrix, target):
        M = len(matrix)
        if M == 0:
            return False
        n = len(matrix[0])
        end = M * n - 1 # total elements
        start = 0
        while start <= end:
            mid_point = start + end // 2
            mid_element = matrix[mid_point//n][mid_point % n]
            if mid_element == target:
                return True
            elif target < mid_element:
                end = mid_point - 1
            else:
                start = mid_point + 1
        return False

obj = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
print(obj.searchMatrix(matrix,target))





