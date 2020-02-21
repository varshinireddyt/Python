"""
Solution 1.6:  Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than
the original string, your method should returnvthe original string. You can assume the string has only uppercase
and lowercase letters (a - z).
"""

def doCompression(s):
    n = len(s)
    i = 0
    temp = []

    while i < n:
        count = 1
        while i < n-1 and s[i] == s[i+1]:
            count +=1
            i += 1
        temp.append(s[i] + str(count))
        i += 1
    return min(s,''.join(temp),key=len)

s = 'aaabbbcaa'
# doCompression(str)
print(doCompression(s))

