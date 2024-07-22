class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        def dfs(i, j):
            nonlocal visited
            nonlocal grid

            if (i,j) in visited or grid[i][j] == "0":
                return 0

            visited.add((i,j))
            # go top
            if j > 0:
                dfs(i,j -1)
            #go down
            if j < len(grid[0]) -1:
                dfs(i, j + 1)
            #go left
            if i > 0:
                dfs(i - 1, j)

            #go right
            if i < len(grid) -1 :
                dfs(i + 1, j)

        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in visited and grid[x][y] != "0":
                    dfs(x,y)
                    count += 1

        return count
        