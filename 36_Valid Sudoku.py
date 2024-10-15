class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visitedR = set()
        visitedC = set()
        visitedGrid = set()

        gridCenter = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        for gRow,gCol in gridCenter:
            if board[gRow][gCol].isdigit():
                visitedGrid.add(board[gRow][gCol])
            
            for dr,dc in directions:
                newR, newC = gRow + dr, gCol + dc
                if board[newR][newC].isdigit() and board[newR][newC] in visitedGrid:
                    return False
                if board[newR][newC].isdigit():
                    visitedGrid.add(board[newR][newC])
            visitedGrid.clear()
        
        for row in range(9):
            for col in range(9):
                if board[row][col].isdigit() and board[row][col] in visitedR:
                    return False
                if board[row][col].isdigit():
                    visitedR.add(board[row][col])
            visitedR.clear()

        for col in range(9):
            for row in range(9):
                if board[row][col].isdigit() and board[row][col] in visitedC:
                    return False
                if board[row][col].isdigit():
                    visitedC.add(board[row][col])
            visitedC.clear()
        return True
                
