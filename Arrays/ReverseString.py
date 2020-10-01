"""
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

class Solution(object):
    def reverseString(self, s):
        self.helper(0,s)

    def helper(self,index,s):
        if s is None or index >= len(s)//2:

            return
        temp = s[index]
        s[index] = s[len(s) - 1 - index]
        s[len(s)-1-index] = temp
        self.helper(index+1,s)

class Solution(object):
    def reverseString(self, s):

        def helper(start,end,str):
            if start >= end:
                return
            str[start], start[end] = start[end], start[start]
            return helper(start+1,end-1,str)
        helper(0,len(s)-1,s)






reverse = Solution()
s = ["h","e","l","l","o"]
reverse.reverseString(s)