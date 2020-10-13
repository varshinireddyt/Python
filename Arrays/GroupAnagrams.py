"""
Leetcode 40: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""
#Time complexity: O(N nlogn) N- length of string, n- length of each string, for sort its O(N) and for sortinf each string O(n log n)
from collections import defaultdict #using default dict to avoid key error
class Solution:
    def groupAnagrams(self, strs):
        dict = defaultdict(list)
        for s in strs:
            dict[tuple(sorted(s))].append(s)

        return dict.values()

strs = ["eat","tea","tan","ate","nat","bat"]
obj = Solution()
print(obj.groupAnagrams(strs))