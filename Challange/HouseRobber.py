"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

"""
"""
Trivial cases:

If there is one house, the answer is the value of that house.
If there are two houses, the answer is max(house1, house2).
If there are three houses, you can either pick the middle house or the sum of the first and the last house. Therefore, it boils down to max(house3 + house1, house2)
"""
#Using Dynamic Programming
class Solution(object):
    def rob(self, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        house = list()  #creating a list
        house.append(nums[0])
        house.append(max(nums[0],nums[1]))
        i = 2
        while i < len(nums):   #appending the max values
            house.append(max(nums[i]+house[i-2], house[i-1]))
            i+=1
        l = len(house)
        return house[l-1]

#nums = [2,1,1,2]
nums= []
sol = Solution()
print(sol.rob(nums))