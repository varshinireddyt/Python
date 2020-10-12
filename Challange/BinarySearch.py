"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
target in nums. If target exists, then return its index, otherwise return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
#using binary search, Time complexity: O(logn)
class Solution:
    def search(self, nums, target):
        min_index = 0
        max_index = len(nums)-1
        while min_index <= max_index:
            mid = (min_index + max_index) // 2
            if nums[mid] < target:
                min_index = mid+1
            elif nums[mid] > target:
                max_index = mid-1
            else:
                return mid
        return -1


obj = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print(obj.search(nums,target))



