class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkTime(currEatSpeed):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas/currEatSpeed)
            
            return hours <= h


        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2

            if checkTime(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left 



        