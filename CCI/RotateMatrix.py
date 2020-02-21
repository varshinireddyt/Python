"""
Solution 1.7 Rotate Matrix by 90 degrees / LeetCode 48: Rotate Image
1. Transpose matrix
2. Reverse rows
"""
def rotate(m):
    m_transpose = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    n = len(m[0])
    for i in range(n):
        for j in range(n):
            temp = m[i][j]
            m[i][j] = m_transpose[j][n-1-i]
            m_transpose[j][n-1-i] = temp
    return m_transpose
"""
Method 2: without using transpose matrix
"""
def rotateNinty(matrix):
    n = len(matrix[0])
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i]= temp
    return matrix

m = [[1,2],[3,4]]
a = [[1,2,3],
  [4,5,6],
  [7,8,9]]
# print(rotate(a))
print(rotateNinty(a))


