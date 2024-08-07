from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)
        result = [[0] * m for _ in range(n)] 
        queue = deque()
        visited = set()
        directions = [(1,0), (0,1), (0,-1),(-1,0)]

        for vertical in range(n):
            for horizontal in range(m):
                if mat[vertical][horizontal] == 0:
                    result[vertical][horizontal] = 0
                    queue.append((vertical,horizontal))
                    visited.add((vertical,horizontal))
                else:
                    result[vertical][horizontal] = -1
        while queue:
            (v,h) = queue.popleft()
            for (vy,hx) in directions:
                newV,newH = v + vy,h + hx
                if 0<= newV < n and 0 <= newH <m and (newV,newH) not in visited:
                    result[newV][newH] = result[v][h] + 1
                    queue.append((newV,newH))
                    visited.add((newV,newH))



        return result
