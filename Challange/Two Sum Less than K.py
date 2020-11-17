class Solution:

#Approach 1: using brute force
    # def twoSumLessThanK(self,A,K):
    #     S = -1
    #     for i in range(len(A)):
    #         temp = 0
    #         for j in range(i+1,len(A)):
    #             temp = A[i] + A[j]
    #             if temp < K:
    #                 S = max(temp,S)
    #
    #     return S

#Approach 2: Two Pointers
    def twoSumLessThanK(self,A,K):
        S = -1
        beg = 0
        end = len(A)-1
        A = sorted(A)
        while beg < end:
            temp = 0
            temp = A[beg] + A[end]
            if temp < K:
                S = max(temp,S)
                beg += 1
            else:
                end -= 1
        return S


A = [34,23,1,24,75,33,54,8]
K = 60
# A = [10, 20, 30]
# K = 15
obj = Solution()
print(obj.twoSumLessThanK(A,K))