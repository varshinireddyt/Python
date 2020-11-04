"""You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.
NOTE: + refers to string concatenation.
Example
For s = "xzxzx", the output should be countWaysToSplit(s) = 5.
Consider all the ways to split s into three non-empty parts:
• If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
• If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
• If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
• If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
• If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
• If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
Since there are five valid ways to split s, the answer is 5.
Input/Output
• [execution time limit] 3 seconds (java)
• [input] string s
A string to split.
Guaranteed constraints:
3 ≤ s.length ≤ 100.
• [output] integer
The number of ways to split the given string.
"""
def countWaysToSplit(s):
    i = 0
    j = 1
    k = 2
    count = 0
    while k < len(s) and j < len(s)-1:
        if k < len(s)-1:
            a = s[i]
            b = s[j:k]
            c = s[k:]
            if a+b != b+c or b+c != c+a or a+b != c+a :
                count += 1
        if k == len(s)-1:
            a = s[i:j]
            b = s[j:k]
            c = s[k:]
            if a + b != b + c or b + c != c + a or a + b != c + a:
                count += 1

            j += 1
        else: k+=1
    return count

s =  "ababa"
print(countWaysToSplit(s))
















