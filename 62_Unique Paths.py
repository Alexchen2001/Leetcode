class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):

            if (row,col) == (0,0):
                return 1
            ways = 0

            if row > 0:
                ways += dp(row - 1 , col)
            if col > 0:
                ways += dp(row, col - 1)
            
            return ways
        return dp(m -1, n -1)

        