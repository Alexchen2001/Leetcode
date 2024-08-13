from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reverseArr = [ -sItem for sItem in stones]
        heapify(reverseArr)
        while len(reverseArr) > 1:
            stone1 = abs(heappop(reverseArr))
            stone2 = abs(heappop(reverseArr))
            if stone1 != stone2:
                heappush(reverseArr, - (stone1 - stone2))
        
        if len(reverseArr) == 1:
            return - reverseArr[0]
        return -1