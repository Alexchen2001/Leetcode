from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = set((0,0,k)) # (vertical, horizontal, steps taken)
        queue = deque([(0,0,0,k)])
        directions = [(1,0),(0,1), (-1,0), (0,-1)]
        vMax,hMax = len(grid), len(grid[0])
        def valid(vertical, horizontal):
            return 0 <= vertical < vMax and 0 <= horizontal < hMax
        while queue:
            (v,h,stepsTaken,skipRemain) = queue.popleft()
            if v == vMax -1 and h == hMax -1:
                return stepsTaken

            for (addV, addH) in directions:
                nextV,nextH = v + addV, h + addH
                if valid(nextV,nextH):
                    if grid[nextV][nextH] == 0:
                        if (nextV,nextH,skipRemain) not in visited:
                            queue.append((nextV,nextH,stepsTaken + 1,skipRemain))
                            visited.add((nextV,nextH,skipRemain))
                    else: # when grid[nextV,nextH] == 1
                        if skipRemain and (nextV,nextH,skipRemain -1 ) not in visited:
                            queue.append((nextV,nextH,stepsTaken + 1,skipRemain -1))
                            visited.add((nextV,nextH,skipRemain -1))
        return -1



                

                

            











