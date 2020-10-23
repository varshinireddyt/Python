"""
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists,
then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds,
 ArrayReader.get will return 2147483647.

 Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""




# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        if reader.get(0) == target:
            return 0
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right = right * 2
        while left <= right:
            mid = left + ((right - left) / 2)
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1