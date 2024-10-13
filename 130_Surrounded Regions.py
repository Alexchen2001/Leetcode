from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(givenR,givenC):
            return 0 <= givenR < m and 0 <= givenC < n
        def dfs(r,c):
            nonlocal tempVisited
            nonlocal isCorner
            
            if r == 0 or r == m - 1 or c == 0 or c == n -1:
                isCorner = True
            
            for dr,dc in directions:
                newR, newC = r + dr, c + dc
                if valid(newR,newC) and (newR,newC) not in tempVisited:
                    if board[newR][newC] == "O":
                        tempVisited.add((newR,newC))
                        dfs(newR,newC)
        
        m = len(board)
        n = len(board[0])
        visited = set()
        tempVisited = set()
        isCorner = False
        directions = [(1,0),(0,1), (-1,0), (0,-1)]
        for row in range(m):
            for col in range(n):
                if (board[row][col] == "O") and ((row,col) not in visited):
                    tempVisited.add((row,col))
                    isCorner = False
                    dfs(row,col)
                    if not isCorner:
                        xList = list(tempVisited)
                        for x,y in xList:
                            board[x][y] = "X"
                            visited.add((x,y))
                    else:
                        visited.update(tempVisited)
                        tempVisited.clear()




                
