from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        emptySpace = set()
        queue = deque([])
        visited = set()

        v = len(grid)
        h = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        def isValid(givenH, givenV):
            return 0 <= givenH < h and 0 <= givenV < v
        for i in range(v):
            for j in range(h):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 0:
                    emptySpace.add((i,j))
        res = 0
        while queue:
            qLen = len(queue)
            for _ in range(qLen):
                currV, currH = queue.popleft()
                rotten.add((currV,currH))
                for dV, dH in directions:
                    newV, newH = currV + dV, currH + dH

                    if isValid(newH, newV) and (newV,newH) not in visited:
                        visited.add((newV, newH))
                        if grid[newV][newH] == 1:
                            queue.append((newV,newH))
                        
            if queue:
                res += 1

        if (len(rotten) + len(emptySpace)) != (v * h) :
            return -1
        
        return res



        

