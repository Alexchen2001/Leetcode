from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Correct the order: (row, column, steps)
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, column, steps)
        initialPt = (entrance[0], entrance[1])  # (row, column)
        visited = set()
        visited.add(initialPt)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left
        m = len(maze)  # number of rows
        n = len(maze[0])  # number of columns
        
        def validExit(currR, currC, block):
            nonlocal initialPt, m, n
            return (currR == 0 or currC == 0 or currR == m - 1 or currC == n - 1) and block == "." and (currR, currC) != initialPt
        
        def valid(currR, currC):
            nonlocal m, n, visited
            return 0 <= currR < m and 0 <= currC < n and (currR, currC) not in visited
       
        while queue:
            currR, currC, currStep = queue.popleft()
            print(str(currR) + " " + str(currC) + " " + str(maze[currR][currC]))
            if validExit(currR, currC, maze[currR][currC]):
                return currStep

            for dR, dC in directions:
                newR, newC = currR + dR, currC + dC
                if valid(newR, newC):
                    if maze[newR][newC] == ".":
                        queue.append((newR, newC, currStep + 1))
                        visited.add((newR, newC))
        return -1
