"""
LeetCode 796: Rotate String
Time Complexity: O(n)
"""
class LeftRotate:
    def rotateString(self, s1,s2):
        if len(s1) != len(s2):
            return False
        if len(s1) == 0 and s1 == s2:
            return True
        for d in  range(len(s1)):
            first  = s1[0:d]
            second = s1[d:]
            word = second + first
            if(word == s2):
                return True
        return False

rotate = LeftRotate()

print(rotate.rotateString("",""))
