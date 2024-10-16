class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1] * freq  for freq in range(1, rowIndex + 2)]
        currLevel = 3
        if rowIndex > 1:
            while currLevel <= rowIndex + 1:
                for i in range(1,currLevel - 1):
                    dp[currLevel - 1][i] = dp[currLevel -2][i - 1] + dp[currLevel - 2][i]
                currLevel += 1
        return dp[rowIndex]
