class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(pilesIndex,levelTaken):
            if pilesIndex >= len(piles) or levelTaken <= 0:
                return 0
            # skip
            ans = dp(pilesIndex + 1, levelTaken)
            #Take current pile
            sumNum = 0
            for i in range(min(levelTaken, len(piles[pilesIndex]))):
                sumNum += piles[pilesIndex][i]
                ans = max(sumNum + dp(pilesIndex + 1, levelTaken -i - 1),ans)
            
            return ans
        return dp(0, k)

            




        