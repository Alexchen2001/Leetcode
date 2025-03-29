class TicTacToe:

    def __init__(self, n: int):
        self.rows = [[0,0] for _ in range (n)]
        self.cols = [[0,0] for _ in range (n)]
        self.diagonal = [0,0]
        self.rDiagonal = [0,0]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row][player - 1] += 1
        self.cols[col][player - 1] += 1
        if row == col:
            self.diagonal[player -1] += 1
        if row == (self.n - col - 1):
            self.rDiagonal[player-1] += 1
        
        if self.rows[row][player - 1] == self.n or self.cols[col][player - 1] == self.n or self.diagonal[player -1] == self.n or self.rDiagonal[player-1] == self.n:
            return player 
        else:
            return 0


     
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)