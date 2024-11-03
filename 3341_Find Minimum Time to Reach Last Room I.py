from heapq import heappush, heappop
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime) # rows
        m = len(moveTime[0]) # columns
        def isValid(inputR, inputC):
            return 0 <= inputR < n and 0 <= inputC < m
        queue = []
        heappush(queue, (0, (0,0)))
        directions = [(0,1), (1,0), (-1,0),(0,-1)]
        visited = set()
        visited.add((0,0))

        while queue:
            (val,(row,col)) = heappop(queue)

            if row == n - 1 and col == m -1:
                return val

            for dR, dC in directions:
                newR, newC = row + dR, col + dC
                if isValid(newR, newC) and (newR,newC) not in visited:
                    if moveTime[newR][newC] >= val:
                        heappush(queue, (moveTime[newR][newC] + 1, (newR, newC)))
                        visited.add((newR,newC))
                    else:
                        heappush(queue, (val + 1, (newR, newC)))
                        visited.add((newR,newC))
                        
        return -1
            
            

        
        
        