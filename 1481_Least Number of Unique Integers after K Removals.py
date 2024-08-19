from collections import Counter
from heapq import heappush, heappop
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        heap = []

        for frequency in counts.values():
            heappush(heap,frequency)
        while k > 0 and len(heap) > 0:
            freq = heappop(heap)
            freq -= 1
            k -= 1
            if freq > 0:
                heappush(heap, freq)
        
        return len(heap)



