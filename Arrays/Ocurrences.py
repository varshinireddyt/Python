"""
Leetcode 1207:
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value
in the array is unique.
"""
def uniqueOccurences(arr):
    temp = set(arr)
    counter = []
    for num in temp:
        count = 0
        for i in arr:
            if num == i:
                count += 1
        if count in counter:
            return False
        else:
            counter.append(count)
    return True



arr = [1,2]

print(uniqueOccurences(arr))