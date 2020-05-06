"""
Leetcode: Given a binary array, find the maximum number of consecutive 1s in this array.
Note: The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Consecutives(object):
    def findMaxConsecutiveOnes(self, nums):
        length = len(nums)-1
        count = 0
        max=0
        if sum(nums) == 0:
            return 0
        for i in range(length):
            j=i+1
            if nums[i] == 1 and nums[i] == nums[j]:
                count += 1
            else:
                count = 0

            if max < count:
                max = count

        return max+1

ones = Consecutives()
# nums = [1,1,0,1,1,1]
# nums = [0,0]
nums = [1,1,0,1]
print(ones.findMaxConsecutiveOnes(nums))


