class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(index, holdStock, remainTrans):
            if index >= len(prices) or remainTrans <= 0:
                return 0 

            ans = dp(index + 1, holdStock, remainTrans)
            if holdStock:
                ans = max(ans,prices[index] + dp(index + 1, False, remainTrans - 1))
            else:
                ans = max(ans, - prices[index] + dp(index + 1, True, remainTrans))
            
            return ans
        
        return dp(0, False, k)
                
            
        