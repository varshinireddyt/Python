"""
LeetCode 3: Longest Substring without repeating characters
example:
 input: "abcabcbb"
 ouput: 3
 Time Complexity: O(n*2)
"""
class LongestSubString:
    def lengthOfLongestSubString(self, s):
        if len(s) == 1:
            return 1
        sub_string = {}
        curr_length = 0
        longest = 0
        sub_start = 0

        for i, c in  enumerate(s):
            if c in sub_string and sub_string[c] >= sub_start:  #considering example sub_start is 0 and sub_string is {a:0}
                sub_start = sub_string[c] + 1  # new substring start which is b i.e  0 + 1
                curr_length = i - sub_string[c] # 3 - 0
                sub_string[c] = i

            else:
                sub_string[c] = i #updating the dictonary
                curr_length += 1
                if curr_length > longest:
                    longest = curr_length

        return longest

subString = LongestSubString()
print(subString.lengthOfLongestSubString("abcabcbb"))



