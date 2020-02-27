"""
Solution 1.8: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
LeetCode 73: Set Matrix Zeroes
"""

class ZeroMatrix:

    def setZeroes(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        # setting flag corner row columns
        row_flag = False
        for i in range(m):
            if matrix[i][0] == 0:
                row_flag = True
        col_flag = False
        for j in range(n):
            if matrix[0][j] == 0:
                col_flag = True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if row_flag == True:
             for i in range(m):
                 matrix[i][0] = 0
        if col_flag == True:
            for j in range(n):
                matrix[0][j] = 0
        return matrix


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
zero = ZeroMatrix()
print(zero.setZeroes(matrix))
# zero.setZeroes(matrix)







