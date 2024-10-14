class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dead = []
        alive = []
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        m = len(board)
        n = len(board[0])
        def valid(givenR,givenC):
            return 0 <= givenR < m and 0 <= givenC < n and board[givenR][givenC] == 1
        
        for i in range(m):
            for j in range(n):
                count = 0
                for dr,dc in directions:
                    newR, newC = i + dr, j + dc
                    if valid(newR,newC):
                        count += 1
                if count < 2 and board[i][j] == 1:
                    dead.append((i,j))
                elif count == 3 and board[i][j] == 0:
                    alive.append((i,j))
                elif board[i][j] == 1 and count > 3:
                    dead.append((i,j))
        for aliveR,aliveC in alive:
            board[aliveR][aliveC] = 1
        for deadR,deadC in dead:
            board[deadR][deadC] = 0