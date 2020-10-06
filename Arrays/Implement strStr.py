"""
Leetcode 28: Implement strStr()
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Input: haystack = "", needle = ""
Output: 0


"""

class Solution(object):

    # approach 1 by slicing the substring O((N-n)n)
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        n, N = len(needle), len(haystack)
        for i in range(N):
            if haystack[i:i+n] == needle:
                return i
        return -1

    # approach 2 by two pointers, time complexity: O((N-n)n)
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        n, N = len(needle), len(haystack)
        i = 0
        while i < N - n + 1:
            #position of the first string of needle in haystack
            while i < N - n + 1 and haystack[i] != needle[0]:
                i += 1

            count = j = 0 #maximum length of the matched string
            while j < n and i < N and haystack[i] == needle[j]:
                i += 1
                j += 1
                count += 1

            if count == len(needle):  #if whole string is found returns start index position
                return i - n

            #otherwise backtrack
            i = i - count + 1

        return -1

haystack = "mississippi"
needle = "issip"
# haystack = "hello"
# needle = "ll"
haystack = "aaaaa"
needle = "bba"
# haystack = ""
# needle ="a"
check = Solution()
print(check.strStr(haystack,needle))