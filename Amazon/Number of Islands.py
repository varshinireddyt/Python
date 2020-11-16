"""
Leetcode 200: Number of islands
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
 You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid):
        if len(grid) == 0 or grid  == None:
            return 0
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numIslands += self.dfs(grid,i,j)

        return numIslands



    def dfs(self,grid, i, j):
        if (i < 0 or i >= len(grid)) or j < 0 or  j >= len(grid[i]) or grid[i][j] == '0':
            return 0

        grid[i][j] = '0'  # if value is 1 then before exploring it's neighbor nodes, we're setting current value to 0
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j )
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        return 1

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
print(obj.numIslands(grid))