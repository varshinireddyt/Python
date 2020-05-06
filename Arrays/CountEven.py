"""
Leetcode: Given an array nums of integers, return how many of them contain an even number of digits.

"""
class CountEven:
    def findNumbers(self,nums):
        length = len(nums)
        even = 0
        for i in range(length):
            count = 0
            while nums[i] != 0:
                nums[i] = nums[i] / 10
                count += 1
            if count % 2 == 0:
                even += 1
        return even

findEven = CountEven()
nums = [12,345,2,6,7896]
print(findEven.findNumbers(nums))