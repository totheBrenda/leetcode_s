## https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                c = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
                if c.count("B") != 2: return True
        return False