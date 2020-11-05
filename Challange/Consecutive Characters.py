class Solution:
#Time Complexit:O(N2)
    def maxPower(self, s):
        maxPower = 1

        for i in range(len(s)):
            count = 1
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    count+=1
                else:
                    break
            if count > maxPower:
                maxPower = count

        return maxPower


    def maxxPower(self,s):

        maxPower = 0
        count = 0
        previous = None
        for i in s:
            if i == previous:
                count += 1
            else:
                previous = c
                count = 1
            maxPower = max(count,maxPower)
        return maxPower




obj = Solution()
s = "leetcode"
s = "abbcccddddeeeeedcba"
s = "hooraaaaaaaaaaay"
s = "tourist"
print(obj.maxPower(s))



