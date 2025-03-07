class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        gLen = len(grid)
        repeated = None
        visited = set()
        exist = set()
        maxVal = gLen * gLen

        for num in range(1, maxVal + 1):
            exist.add(num)
        
        for h in range(gLen):
            for v in range(gLen):
                if grid[h][v] in visited: 
                    repeated = grid[h][v]
                else:
                    visited.add(grid[h][v])
                    exist.remove(grid[h][v])
        
        res = [repeated,exist.pop()]
        return res