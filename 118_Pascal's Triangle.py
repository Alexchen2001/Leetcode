class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * freq for freq in range(1,numRows + 1)]
        currLevel = 3
        if numRows > 2:
            while currLevel <= numRows:
                for i in range(1,currLevel- 1):
                    dp[currLevel - 1][i] = dp[currLevel - 2][i - 1] + dp[currLevel - 2][i]
                currLevel += 1
        
        return dp