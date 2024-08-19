from heapq import heappush, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital,profits))
        heap = []
        i = 0


        for _ in range(k):
            # you need to check whether if our capital allows us to do the project
            # only runs when the project has enough capital
            while i < n and projects[i][0] <= w:
                # since the the capital do not decrease, we can always start a project that 
                #requires the amount of capital, so we only care about profit to raise capital
                heappush(heap, -projects[i][1])
                i += 1

            if len(heap) == 0:
                return w
            w = w + (- heappop(heap))
        return w

            



