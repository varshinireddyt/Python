"""
Solution 1.9: String Rotation:
"""
#Solution 1
def isSubString(s1,s2):
    if len(s1) != len(s2):
        return False
    s = s1 + s2
    if s2 in s:
        return True
    else:
        return False

#Solution 2
def findString(s1,s2):
    if len(s1) != len(s2):
        return False
    s = s1 + s2
    return s.find(s2)!= False

s1 = "waterbottle"
s2 = "erbottlewat"

print(findString(s1,s2))