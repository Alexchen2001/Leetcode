class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(index):
            
            # base case
            if index <= 1:
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index] = min(dp(index -1) + cost[index - 1], dp(index-2) + cost[index -2])
            return memo[index]

        memo = {}
        return dp(len(cost))

        