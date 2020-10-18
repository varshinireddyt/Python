""""
Leetcode 912. Sort an Array

Given an array of integers nums, sort the array in ascending order.

"""""

class Solution:

#Using merge sort, Timecomplexity: O(n log n)
    def sortArray(self, nums):

        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]
            self.sortArray(left)
            self.sortArray(right)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
                k += 1
            # if only one element left
            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1

        return nums

    def doQuickSort(self,nums):


        N = len(nums)












li = Solution()
#nums = [5,2,3,1]
nums = [5,1,1,2,0,0]

print(li.sortArray(nums))







