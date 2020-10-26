"""
Leetcode: Champagne Tower
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.
 Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will
fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured,
the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.
After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally,
and each will get half cup of champange.
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        dp = [[0 for _ in range(x)] for x in range(1, query_row + 2)]   #assigning 0 for all the the glasses
        dp[0][0] = poured   #intial
        for i in range(query_row):
            for j in range(len(dp[i])):
                temp = (dp[i][j] - 1) / 2.0   # since each glass divides the liquid into two parts after it's being fulled
                if temp > 0:
                    dp[i + 1][j] += temp    # incrementing in the left side of the glass
                    dp[i + 1][j + 1] += temp   # incrementing the right side of the glass

        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1

poured = 1
query_row = 1
query_glass = 1

obj = Solution()
print(obj.champagneTower(poured,query_row,query_glass))