from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        visited = set()
        visited.add((0,0))
        queue = deque([(0,0,1)]) # (verticalCoord,horizontalCoord,step)
        direction = [(1,0), (0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        def validCheck(col, row):
                return 0 <= row < n and 0 <= col < n and grid[col][row] == 0
        
        while queue:
            col, row, step = queue.popleft()

            if (col,row) == (n-1, n-1):
                return step
            
            for dx, dy in direction:
                next_col,next_row = col + dy, row + dx

                if validCheck(next_col, next_row) and (next_col,next_row) not in visited:
                    visited.add((next_col,next_row))
                    queue.append((next_col,next_row,step + 1))
        
        return -1


