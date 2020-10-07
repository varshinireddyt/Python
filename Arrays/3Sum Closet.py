"""
Leetcode 16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
 Return the sum of the three integers. You may assume that each input would have exactly one solution.
 Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 """

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        close = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)):
            beg, end = i+1, len(nums)-1
            while beg < end:
                sum = nums[i] + nums[beg] + nums[end]
                if sum == target:
                    return sum
                if abs(sum-target) < abs(close - target):
                    close = sum
                if sum < target:
                    beg += 1
                else:
                    end -= 1
        return close
sum = Solution()
nums = [1,1,-1,-1,3]
target = 3
print(sum.threeSumClosest(nums,target))