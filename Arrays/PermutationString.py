"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
"""
from collections import defaultdict
import string
def checkInclusion(s1,s2):

    #dic = defaultdict(int)

    temp = dict(zip(string.ascii_lowercase, range(1, 27)))
    temp = dict.fromkeys(temp, 0)





s1 = 'ab'
s2 = 'ab'
print(checkInclusion(s1,s2))




