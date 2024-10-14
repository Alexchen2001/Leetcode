class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroZone = []
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroZone.append((i,j))
                
        for row, col in zeroZone:
            for j in range(n):
                matrix[row][j] = 0
            for i in range(m):
                matrix[i][col] = 0
