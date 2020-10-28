from collections import defaultdict
class Solution:

#Approach1 using defaultdict() --> 47% faster
    # def lengthOfLongestSubstringTwoDistinct(self,s):
    #     if len(s) <= 2:
    #         return len(s)
    #     longest = 2
    #     sub_start = 0
    #     sub_string = defaultdict()
    #     sub_end = 0
    #
    #     while sub_end < len(s):
    #         if len(sub_string) <= 2:
    #             sub_string[s[sub_end]] = sub_end
    #             sub_end +=1
    #         if len(sub_string) >= 3:
    #             #delete the left most/newely added char
    #             del_char = min(sub_string.values())
    #             del sub_string[s[del_char]]
    #             #updating the start pointer
    #             sub_start = del_char + 1
    #         longest = max(longest,abs(sub_start-sub_end))
    #
    #     return longest


# approach 2: using dict() ---> 97% faster
    def lengthOfLongestSubstringTwoDistinct(self,s):
        start,end = 0,0
        longest = 0
        subString = dict()
        while end < len(s):
            subString[s[end]] = end
            if len(subString) > 2:
                index = min(subString.values())
                subString.pop(s[index])
                start = index + 1
            longest = max(longest,end-start + 1)
            end += 1
        return longest


obj = Solution()
s = "eceba"
s = "ccaabbb"
s = 'aaaa'
print(obj.lengthOfLongestSubstringTwoDistinct(s))


