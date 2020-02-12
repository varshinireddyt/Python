"""
Problem 1.2: Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.

Solution 1: Using Sorting
In order to sort the string here i have used bubble sort.
Time Complexity of Bubble Sort: O(n*2)
"""
def sortString(s):
    l = []
    for i in range(0,len(s)):
        l.append(s[i])
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if l[i] < l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

def checkPermutation(s1,s2):
    if len(s1) != len(s2):
        return False
    x = sortString(s1) #sorted string 1
    y = sortString(s2) #sorted string 2
    return x == y

s1 = 'abc'
s2 = 'cbad'
print(checkPermutation(s1,s2))
