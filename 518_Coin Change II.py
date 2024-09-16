class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(index, amount):
            if amount == 0:
                return 1
            if index == len(coins):
                return 0
            if memo[index][amount] != -1:
                return memo[index][amount]
            

            if coins[index] > amount:
                memo[index][amount] = dp(index + 1, amount)
            else:
                memo[index][amount] = dp(index, amount - coins[index]) + dp(index + 1, amount)
            
            return memo[index][amount]

        memo = [[-1]* (amount + 1) for _ in range(len(coins))]
        return dp(0, amount)
            
