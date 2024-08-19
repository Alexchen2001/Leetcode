from heapq import heappush, heappop
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = [(- boxType[1],boxType[0]) for boxType in boxTypes]
        heapify(boxTypes)
        res = 0
        
        while truckSize > 0 and len(boxTypes) > 0:
            (units, boxes) = heappop(boxTypes)
            res -= units
            boxes -= 1
            truckSize -= 1
            if boxes > 0:
                heappush(boxTypes, (units, boxes))
        return res
                







        