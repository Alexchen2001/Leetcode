class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        result = 0
        tempArea = 0

        def dfs(v,h):
            nonlocal visited
            nonlocal tempArea
            nonlocal grid

            if (v,h) in visited or grid[v][h] == 0:
                return 0
            visited.add((v,h))
            if grid[v][h] == 1:
                tempArea += 1
            
            # go left
            if h > 0:
                dfs(v, h - 1)
            #go right
            if h < len(grid[0]) - 1:
                dfs(v, h + 1)
            # go up 
            if v > 0:
                dfs(v - 1, h)
            # go down
            if v < len(grid) - 1:
                dfs(v + 1, h)



        for vertical in range(len(grid)):
            for horizontal in range(len(grid[0])):
                if grid[vertical][horizontal] != 0 and (vertical,horizontal) not in visited:
                    dfs(vertical,horizontal)
                    if tempArea > result:
                        result = tempArea
                    tempArea = 0
        return result


