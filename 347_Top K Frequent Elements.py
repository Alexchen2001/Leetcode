from heapq import * 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        ans = []

        for key, val in counts.items():
            heappush(heap, (-val, key))

        
        for _ in range(k):
            ans.append(heappop(heap)[1])
        
        return ans