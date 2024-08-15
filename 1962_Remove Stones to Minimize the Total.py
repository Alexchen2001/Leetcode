from heapq import *
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)

        for _ in range(k):
            num = - heappop(piles)
            num = int(ceil(num / 2))
            heappush(piles,- num)

        
        return - sum(piles)
