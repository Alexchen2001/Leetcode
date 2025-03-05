class Solution:
    def coloredCells(self, n: int) -> int:
        if n ==1:
            return 1
        dp = {}
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1] + (i * 4)
        return dp[n - 1]