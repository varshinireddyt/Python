"""
Median of Two Sorted Array: Given two sorted arrays nums1 and nums2 of size m and n respectively.
Return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).
"""

def findMedianSortedArrays(num1,num2):
    nums3 = num1 + num2
    nums3 = sorted(nums3)
    l = len(nums3)
    if l % 2 == 0:
        return (nums3[int((l/2) + 0.5)] + nums3[int((l/2) - 0.5)]) / 2
    else:
        return nums3[int(l/2)]

"""
   num3 = num1 + num2
    num3 = sorted(num3)
    l = len(num3)
    if l % 2 == 0:
        return (num3[l//2] + num3[(l//2)-1]) / 2
    else:
         return  num3[l//2]
         """



num1 = [1,2]
num2 = [3,4]
print(findMedianSortedArrays(num1,num2))