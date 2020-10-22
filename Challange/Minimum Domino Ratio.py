class Solution:
    def minDominoRotation(self, A, B):

        def find(target):
            count_A = 0
            count_B = 0
            for i in range(len(A)):

                if A[i] != target and B[i] != target:
                    return -1
                if A[i] != target:
                    count_A +=1
                if B[i] != target:
                    count_B += 1

            return min(count_A,count_B)


        count = find(A[0])
        if count != -1 or A[0] == B[0]:
            return count
        else:
            return find(B[0])






#A = [2,1,2,4,2,2]
#B = [5,2,6,2,3,2]
A = [3,3,1,2,3]
B = [3,6,3,3,4]


obj = Solution()
print(obj.minDominoRotation(A,B))




