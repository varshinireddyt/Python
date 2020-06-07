"""
1.4: Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""


"""
Credits: GeeksforGeeks(lexicographically first palindromic String)
Approach:
1. If length of string is even, then the frequency of each character in the string must be even.
2. If the length is odd then there should be one character whose frequency is odd and all other chars must have even
frequency and at-least one occurrence of the odd character must be present in the middle of the string.
Algorithm:
1. Store frequency of each character in the given string
2. Check whether a palindromic string can be formed or not using the properties of palindromic string mentioned above.

"""
def charValue(c):
    val = ord(c)
    if ord('a') <= val <= ord('z'):
        return val - ord('a')
    elif ord('A') <= val <= ord('Z'):
        return val - ord('A')
    return -1



def findPalindrome(s):
    freq = [0 for _ in range(ord('z') - ord('a') + 1)]
    odd = 0
    for c in s:
        val = charValue(c)
        if val != -1:
            freq[val] += -1
            if freq[val] % 2:
                odd += 1
            else:
                odd -= 1
    return odd <= 1

s = "jhsabckuj ahjsbckj"
print(findPalindrome(s))

# This code is contributed by mits
