from heapq import heappush, heappop
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        #√(x1 - x2)^2 + (y1 - y2)^2)
        def distOrigin(givenX, givenY):
            return sqrt(((givenX - 0)**2) + ((givenY - 0)**2))

        for x,y in points:
            heappush(heap, (- distOrigin(x,y), x, y))
            if len(heap) > k:
                heappop(heap)
            
        return [(point[1],point[2]) for point in heap]
        
