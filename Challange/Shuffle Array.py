"""
Leetcode 1640. Check Array Formation Through Concatenation
or ShufflePieces
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Input: arr = [85], pieces = [[85]]
Output: true

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
"""
class Solution:
    def canFormArray(self, arr, pieces):
        dict = {}
        for i in range(len(arr)):
            dict[arr[i]] = i
        for i  in range(len(pieces)):
            j = 0
            index = dict.get(pieces[i][j])
            if index is None: return False
            sub = len(pieces[i])
            rem = len(arr) - index
            if index is None or sub > rem:
                return False
            while j < len(pieces[i]):
                if pieces[i][j] == arr[index]:
                    index += 1
                    j += 1
                else:
                    return False
        return True

obj = Solution()
arr = [15,88,2]
pieces = [[88,2],[15]]
print(obj.canFormArray(arr,pieces))


