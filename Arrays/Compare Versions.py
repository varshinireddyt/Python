"""
Leetcode 165: Compare Version Numbers
Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
"""

class Solution:

#Approach: split and parse integers,
#Time complexity: n = version2 length, m - version1 length - O(n + m + maxx(n,m))
    def compareVersion(self, version1, version2):
        verOne = version1.split('.')
        verTwo = version2.split('.') # splitting by '.'
        m = len(verOne)
        n = len(verTwo)
        verOne = [int(i) for i in verOne]  # coverting the strings in list to integers
        verTwo = [int(i) for i in verTwo]
        if m > n:
            for i in range(n,m):
                verTwo.append(0)   # appending 0 to the one which has less length
        elif n > m:
            for i in range(m,n):
                verOne.append(0)
        for i in range(len(verOne)):  # comparing which version is greater
            if verOne[i] > verTwo[i]:
                return 1
            elif verTwo[i] > verOne[i]:
                return -1
        return 0


version1 = "1.01"
version2 = "1.001"
obj = Solution()
print(obj.compareVersion(version1,version2))
