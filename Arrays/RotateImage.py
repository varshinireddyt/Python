"""
Leetcode 48: Rotate Image
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Matrix rotation by 90 degrees clockwise

Solution:
Hint
1. 90 degreees clockwise: first transpose, then reverse rows
2. 90 degrees anticlockwise: first transpose, then reverse columns
"""


class Solution:
    def rotate(self, matrix):
        matrix = self.transpose(matrix)
        for i in range(len(matrix[0])):
            matrix[i] = matrix[i][::-1]
        return matrix

    def transpose(self,matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix




matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotation = Solution()
print(rotation.rotate(matrix))

"""
m[0][0] = m[l-1 - 0][0]
m[0][1] = m[l-1-1][0]

m[i][j] = m[l-i-1][0]

"""