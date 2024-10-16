class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def F(i):
            if i == 0:
                return memo[0]
            if i == 1:
                return memo[1]
            if i == 2:
                return memo[2]
            
            if i in memo:
                return memo[i]
            else:
                memo[i] = F(i - 1) + F(i -2)
            return memo[i]

        F(n)
        return memo[n]