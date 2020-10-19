
"""
Trivial cases:

If there is one house, the answer is the value of that house.
If there are two houses, the answer is max(house1, house2).
If there are three houses, you can either pick the middle house or the sum of the first and the last house. Therefore, it boils down to max(house3 + house1, house2)

divide the array into two parts- ine leaving the last element (nums[:-1]), leaving the first element(nums[1:])
"""

class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_circle(nums[1:]),self.rob_circle(nums[:-1]))

    def rob_circle(self,nums):
        rob = 0
        temp = 0
        for curr in nums:
            swap = rob
            rob = max(curr + temp, rob)
            temp = swap
        return rob



obj = Solution()
#nums = [2,3,2]
nums = [1,2,3,1]
print(obj.rob(nums))

