"""
LeetCode 5: Longest Palindromic Substring
example:
input: "babad"
Ouput: can be "bab" or "aba"
Time Complexity: O(n*2)
"""

class LongestPalindrome:
    def findLongestPalindrome(self, s:str) -> str:
        if len(s) == 1:
            return s
        longest = 0
        curr_length = 0
        sub_string = ""
        palindrome = ""
        for i in range(len(s)):
            count = 0
            for j in range(i+1,len(s)):
                if count == 0:
                    sub_string =  s[i] + s[j]
                    count += 1
                else:
                    sub_string = sub_string + s[j]
                    count += 1
                if sub_string == sub_string[::-1]:
                    curr_length = len(sub_string)
                    if curr_length > longest:
                        longest = curr_length
                        palindrome = sub_string
            if palindrome ==  "":
                palindrome = s[i]

        return palindrome

subString = LongestPalindrome()
print(subString.findLongestPalindrome("ac"))