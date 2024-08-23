class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        def valid(row, column):
            return 0 <= row < m and 0 <= column < n

        def checkMat(effort):
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            stack = [(0,0)]
            seen = {(0,0)}

            while stack:
                currR, currC = stack.pop()
                if (currR, currC) == (m -1, n -1):
                    return True
                
                for dx, dy in directions:
                    newR,newC = currR + dx, currC + dy
                    if valid(newR, newC) and (newR, newC) not in seen:
                        if abs(heights[newR][newC] - heights[currR][currC]) <= effort:
                            seen.add((newR,newC))
                            stack.append((newR,newC))
            return False
            
        left, right = 0, max(max(rowArr) for rowArr in heights)
        while left <= right:
            mid = (left + right) // 2
            
            if checkMat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


