class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dp (row, col):
            if (row,col) == (0,0):
                return 1
            ways = 0
            if row > 0:
                if obstacleGrid[row -1][col] == 0:
                    ways += dp(row - 1, col)
            if col > 0:
                if obstacleGrid[row][col -1] == 0:
                    ways += dp(row, col - 1)
            
            return ways
        m = len(obstacleGrid) -1
        n = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[m][n] == 1:
            return 0
        return dp(m, n)


        