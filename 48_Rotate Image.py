class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        res = []
        directions = [(0,1),(1,0), (0,-1),(-1,0)]
        visitedA = set()
        row = 0
        col = -1
        totalLength = n * n
        while len(res) < totalLength:
            for dr,dc in directions:
                if dc == 1:
                    col += dc
                    while col < n and (row,col) not in visitedA:
                        res.append(matrix[row][col])
                        visitedA.add((row,col))
                        col += dc
                    col -= dc
                
                elif dr == 1:
                    row += dr
                    while row < n and (row,col) not in visitedA:
                        res.append(matrix[row][col])
                        visitedA.add((row,col))
                        row += dr
                    row -= dr
                elif dc == -1:
                    col += dc
                    while col >= 0 and (row,col) not in visitedA:
                        res.append(matrix[row][col])
                        visitedA.add((row,col))
                        col += dc
                    col -= dc
                else:
                    row += dr
                    while row >= 0 and (row,col) not in visitedA:
                        res.append(matrix[row][col])
                        visitedA.add((row,col))
                        row += dr
                    row -= dr
                
                if len(res) >= totalLength:
                    break
        
        directions = [(1,0), (0,-1),(-1,0),(0,1)]
        visitedA.clear()
        row = - 1
        col = n - 1
        index = 0

        while index < totalLength:
            for dr,dc in directions:
                if dc == 1:
                    col += dc
                    while col < n and (row,col) not in visitedA:
                        matrix[row][col] = res[index]
                        index += 1
                        visitedA.add((row,col))
                        col += dc
                    col -= dc
                
                elif dr == 1:
                    row += dr
                    while row < n and (row,col) not in visitedA:
                        matrix[row][col] = res[index]
                        index += 1
                        visitedA.add((row,col))
                        row += dr
                    row -= dr
                elif dc == -1:
                    col += dc
                    while col >= 0 and (row,col) not in visitedA:
                        matrix[row][col] = res[index]
                        index += 1
                        visitedA.add((row,col))
                        col += dc
                    col -= dc
                else:
                    row += dr
                    while row >= 0 and (row,col) not in visitedA:
                        matrix[row][col] = res[index]
                        index += 1
                        visitedA.add((row,col))
                        row += dr
                    row -= dr
                
                if index >= totalLength:
                    break 
