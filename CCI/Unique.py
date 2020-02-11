"""
Book: Cracking the coding interview
Chapter 1: 1.1 Is Unique
"""

#Solution 1
"""
Time complexity: O(n*2)
"""
def isUnique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] is s[j]:
                return False
    return True
s = 'unique'
print(isUnique(s))


#Solution 2
"""
Time complexity: O(n)
"""
def findUnique(s):
    """ string length cannot be greater than 256"""
    if len(s) > 256:
        return False
    """
    Character set consists of false(128)
    char_set = [false,false,.....]
    """
    char_set = [False for _ in range(128)]
    for char in s:
        val = ord(char) #ord() function is used to convert the character into unicode value
        """
        If the unicode value is repeated then it will return false
        """
        if char_set[val]:
            return False
        char_set[val] = True

    return True

print(findUnique(s))


