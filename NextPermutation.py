"""
LeetCode 31: Next Permutation
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
"""

"""
Algorithm:
1.Find largest index i such that array[i − 1] < array[i].
(If no such i exists, then this is already the last permutation.)

2.Find largest index j such that j ≥ i and array[j] > array[i − 1].

3.Swap array[j] and array[i − 1].

4.Reverse the suffix starting at array[i].

"""

class Solution:

     def nextPermutation(self, nums):
         j = -1
         i = len(nums) - 1
         while i > 0:
            if nums[i-1] < nums[i]:
                j = i-1
                break
            i -= 1
         while nums[j] <= nums[i-1]:
             j -= 1
         nums[i-1], nums[j] = nums[j], nums[i-1]
         nums[i : ] = nums[len(nums) - 1 : i - 1: -1]
         return nums

nums = [3,2,1]
arr = Solution()
print(arr.nextPermutation(nums))






