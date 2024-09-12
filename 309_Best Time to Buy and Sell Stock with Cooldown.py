class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(index, holdStock):
            if index >= len(prices):
                return 0
            
            ans = dp(index + 1, holdStock)
            if holdStock:
                ans = max(ans, prices[index] + dp(index + 2, False))
            else:
                ans = max(ans, -prices[index] + dp(index + 1, True))
            
            return ans
        return dp(0,False)


        w w w