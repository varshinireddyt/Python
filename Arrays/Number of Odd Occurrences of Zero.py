"""
Given an array of positive integers, return the number of integers that contain an odd number of zeros.

Example: a = [5, 10, 200, 10070, 56]
Output: 2 (because 10 has one zero and 10070 has three zeros). The other numbers have an even number of zeroes.
"""
def oddZeros(arr):
    count = 0
    for num in arr:
        odd = 0
        for i in str(num):
            if int(i) == 0:
                odd += 1
        if odd % 2 != 0:
            count += 1

    return count

arr = [5, 10, 200, 10070, 56]
print(oddZeros(arr))
