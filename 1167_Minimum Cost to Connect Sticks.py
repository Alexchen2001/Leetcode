from heapq import heappush, heappop, heapify
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        if len(sticks) == 0:
            return 0

        while len(sticks) > 1:
            stick1 = heappop(sticks)
            stick2 = heappop(sticks)
            cost = cost + stick1 + stick2
            heappush(sticks, stick1 + stick2)

        return cost
        