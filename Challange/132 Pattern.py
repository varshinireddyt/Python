class Solution(object):
    def find132pattern(self, nums):
        if len(nums) <= 2:
            return False
        i = nums[0]
        for j in range(1, len(nums)-1):
            if nums[j] > i:
                for k in range(j + 1, len(nums)):
                    if nums[k] > i and nums[k] < nums[j]:

                        return True
                    else:
                        i = nums[j]
        return False


obj = Solution()
# nums = [1, 2, 3, 4]
nums = [3,1,4,2]
#nums = [-1, 3, 2, 0]
print(obj.find132pattern(nums))
