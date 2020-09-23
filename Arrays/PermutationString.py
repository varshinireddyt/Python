"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
"""
from collections import Counter
def checkInclusion(s1,s2):
    l1,l2 = len(s1), len(s2)
    if s2 is None or s2 is None:
        return False
    s1_count = Counter(s1)   #stores the count of s1 string
    for i in range(0,l2-l1+1):
        s2_char = s2[i:i+l1]   #sliding the s2 string by the length of s1 string
        s2_count = Counter(s2_char) #storing the count of slided string
        if s2_count == s1_count:    #comparing the two counters
            return True
    return False

s1 = 'aba'
s2 = "eidbaooo"
print(checkInclusion(s1,s2))












