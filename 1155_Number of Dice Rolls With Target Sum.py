class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        dp[0][0] = 1
        MOD = 10**9 + 7

        # how many dices left 
        for i in range(1, n + 1):
            # iteration of target
            for j in range(1, target + 1):
                # if the remainder of the target is smaller than the face of the dice
                # there is no meaning in it
                for f in range(1, min(k + 1, j + 1)):
                    # current ways of dice faces + remainder iteration
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - f]) % MOD
        
        return dp[-1][-1]



