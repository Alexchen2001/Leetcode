class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = max(candies)
        n = len(candies)
        def checkTotal(givenK):
            count = 0
            if givenK == 0:
                return n
            for candy in candies:
                if givenK <= candy:
                    count += (candy // givenK)
            return count
        low = 0 
        high = total

        while low < high:
            mid = (low + high + 1) // 2
            print(mid)
            if checkTotal(mid) >= k:
                low = mid
                
            else:
                high = mid - 1
        
        return low
