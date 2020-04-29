"""
Leetcode: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i] + nums[j] :
                  res = [i,j]
                  return res
    # Using Dictionary

    def twoSumHash(self,nums,target):
        dict = {}
        for k,v in enumerate(nums):
            if v in dict:
                return [dict[v],k]
            else:
                dict[target-nums[k]] = k








nums = [3,3]
target = 6
sum = Solution()
# print(sum.twoSum(nums,target))
print(sum.twoSumHash(nums,target))

