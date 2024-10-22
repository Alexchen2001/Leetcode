class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0] * n for _ in range(n)] 
        def isValid(r,c):
            return 0 <= r < n and 0 <= c < n

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        row = 0
        col = 0
        res[0][0] = 1

        count = 2
        while count <= n**2:
            for dr, dc in directions:
                while isValid(row + dr,col + dc) and res[row + dr][col + dc] == 0:
                    newR, newC = row + dr, col + dc
                    res[newR][newC] = count
                    count += 1
                    row, col = newR, newC
        return res
                