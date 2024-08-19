from heapq import * 
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            heappush(heap, (-abs(x - num), -num))
            if len(heap) > k:
                heappop(heap)
        
        return sorted([-z[1] for z in heap])

        