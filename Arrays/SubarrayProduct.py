"""
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

Approach: Sliding Window
Our loop invariant is that left is the smallest value so that the product in the window prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.

For every right, we update left and prod to maintain this invariant. Then, the number of intervals with subarray product less than k and with right-most coordinate right,
is right - left + 1. We'll count all of these for each value of right

"""

def numSubarrayProduct(nums,k):
    if k <= 1: return 0
    product = 1
    count = j = 0    # here j is right, i is left acc to aproach
    for i in range(len(nums)):
        product *= nums[i]
        while product >= k:
            product /= nums[j]
            j += 1
        count += i - j + 1
    return count

nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProduct(nums,k))

