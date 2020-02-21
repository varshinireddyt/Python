"""
LeetCode 443: String Compression
"""
class Solution(object):
    def compress(self,chars):
        """Solution 1: Using extra space
        Time Complexity: O(n*2)
         """
        n = len(chars)
        temp = []
        i = 0
        while i < n:
            count = 1
            while i < n-1 and chars[i] == chars[i+1]:
                count+=1
                i += 1
            if count == 1:
                temp.append(chars[i])
            else:
                temp.append(chars[i])
                temp.append(str(count))
            i+=1
        return temp

    def compression(self,chars):
        """Solution 2: Two pointer solution
        Time Complexity: O(n)"""
        n = len(chars)
        i = j = 0
        while i < n:
            c = chars[i]
            count = 0
            while i < n and chars[i] == c:
                i += 1
                count += 1
            chars[j], j = c, j+1
            if count > 1:
                for k in str(count):
                    chars[j],j = k, j+1
        return j

scompress =  Solution()
chars = ["a","a","b","b","c","c","c"]
# print(scompress.compress(chars))
print(scompress.compression(chars))
