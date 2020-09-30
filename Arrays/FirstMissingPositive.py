"""
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.
Input: [1,2,0]
Output: 3
"""


#using sorted: 
def firstMissingPositive(nums):
    if 1 not in nums:
        return 1
    sorted_nums = sorted(nums)
    i = 0
    while i < len(nums)-1:
        if sorted_nums[i] < 0:
            i += 1
        elif sorted_nums[i+1] - sorted_nums[i]  > 1:
            return sorted_nums[i]+1
        else:
            i+=1

    return sorted_nums[len(nums)-1]+1

#using dictionary: O(n)
def missingPositive(nums):

    if 1 not in nums:
        return 1
    nums_dict = {}
    for num in nums:
        if num >= 1:
            nums_dict[num] = True
    i = 2
    N = len(nums_dict)
    while i <= N+1:
        if i not in nums_dict:
            return i
        else:
            i += 1

#using array: O(n)
def missingPositive(nums):

    if 1 not in nums:
        return 1
    nums_dict = []
    for num in nums:
        if num >= 1:
            nums_dict.append(num)
    i = 1
    N = len(nums_dict)
    while i <= N+1:
        if i not in nums_dict:
            return i
        else:
            i += 1




#nums = [1,2,0]
#nums = [3,4,-1,1]
#nums = [7,8,9,11,12]
nums = [2,1]
print(missingPositive(nums))







