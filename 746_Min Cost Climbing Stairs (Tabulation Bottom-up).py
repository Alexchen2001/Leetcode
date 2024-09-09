class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Tabulation Bottom-up approach
        n = len(cost)
        dpTable = [0] * (n + 1)

        for index in range(2, n + 1):
            dpTable[index] = min(dpTable[index - 1] + cost[index - 1], dpTable[index - 2] + cost[index -2])

        return dpTable[n]
        