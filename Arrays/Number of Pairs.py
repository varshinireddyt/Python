"""
Given a list of int, return number of pairs (index i and j) that satisfy i <= j and list[i] + reverse(list[j]) = list[j] + reverse(list[i]).
So if list[i] = 123 then reverse(list[i]) = 321
"""

def numberOfPairs(num):
    i = 0
    numPair = 0
    while i < len(num):
        for j in range(i,len(num)):
            if num[i] + reverse(num[j]) == num[j] + reverse(num[i]):
                numPair += 1
        i += 1
    return numPair

def reverse(n):
    rev = 0
    while n>0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev

num = [12,1,2]
print(numberOfPairs(num))

