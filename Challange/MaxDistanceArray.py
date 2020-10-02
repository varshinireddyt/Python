"""
Leetcode 624. Maximum Distance in Arrays
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one)
and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|.
Your task is to find the maximum distance.

Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.


Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
def maxDistance(arrays):
    diff = 0
    maximum = arrays[0][len(arrays[0])-1]
    minimum = arrays[0][0]

    for i in range(1,len(arrays)):
        diff = max(diff, max(abs(arrays[i][len(arrays[i])-1]-minimum),abs(maximum-arrays[i][0])))
        minimum = min(minimum,arrays[i][0])
        maximum = max(maximum,arrays[i][len(arrays[i])-1])
    return diff

# arrays = [[1,2,3],
#  [4,5],
#  [1,2,3]]

arrays = [[1,5],[3,4]]
# arrays = [[1,4],[0,5]]
print(maxDistance(arrays))











