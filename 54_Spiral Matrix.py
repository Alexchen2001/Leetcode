class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        row = 0
        col = -1
        totalLength = (m * n)
        res = []
        while len(res) < totalLength:
            for dr, dc in directions:
                if dc == 1:
                    col += dc
                    while col < n and (row,col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row,col))
                        col += dc
                    col -= dc
                elif dr == 1:
                    row += dr
                    while row < m and (row,col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row,col))
                        row += dr
                    row -= dr
                elif dc == -1:
                    col += dc
                    while col >= 0 and (row,col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row,col))
                        col += dc
                    col -= dc
                
                else:
                    row += dr
                    while row >= 0 and (row,col) not in visited:
                        res.append(matrix[row][col])
                        visited.add((row,col))
                        row += dr
                    row -= dr
                
                if len(res) >= totalLength:
                    break
        return res
            

        