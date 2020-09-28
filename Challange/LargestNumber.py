"""
Given a list of non negative integers, arrange them such that they form the largest number.
Example:
Input: [10,2]
Output: "210"
Input: [3,30,34,5,9]
Output: "9534330"
"""
from functools import cmp_to_key
def largestNumber(nums):
    func = lambda a,b: 1 if a + b < b + a else -1 if b + a < a + b else 0
    # s = [str(i) for i in nums]
    # s = list(map(str,nums))
    #s.sorted([str(i) for i in nums],key = cmp_to_key(func))
    return  str(int("".join(sorted([str(i) for i in nums],key = cmp_to_key(func)))))



nums = [3,30,34,5,9]
#nums = [10,2]
print(largestNumber(nums))