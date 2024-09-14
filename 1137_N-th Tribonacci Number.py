class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 1)

        for index in range(n + 1):
            if index == 0:
                dp[0] = 0
            elif index == 1:
                dp[1] =  1
            elif index == 2:
                dp[2] = 1
            else:
                dp[index] = dp[index - 3] + dp[index - 2] + dp[index -1]
        return dp[n]




        # @cache
        # def dp(index):

        #     if index == 0:
        #         return 0
        #     if index == 1:
        #         return 1
        #     if index == 2:
        #         return 1

        #     return dp(index - 3) + dp(index - 2) + dp(index -1)
        # return dp(n)
            

        