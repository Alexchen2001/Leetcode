class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dpT = {}
        @cache
        def dp(currI):
            if currI >= n:
                return 0
            
            if currI in dpT:
                return dpT[currI]

            res = float('-inf')
            total = 0
            for i in range(currI, min(currI + 3, n)):
                total += stoneValue[i]
                res = max(res, total - dp(i + 1))
            dpT[currI] = res
            return res
        
        ans = dp(0)

        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
            
