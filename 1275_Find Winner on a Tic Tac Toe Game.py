class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        As = set()
        Bs = set()
        diagonals = {(0,0), (0,2), (1,1), (2,0), (2,2)}
        n = len(moves)
        As.add((moves[0][0], moves[0][1]))
        def checkForWinner(currPosition, theSet):
            # check for row
            check = 0
            for num in range(3):
                if (currPosition[0], num) in theSet:
                    check += 1
                else:
                    break
            if check == 3:
                return True
            # check for column
            check = 0
            for num in range(3):
                if (num, currPosition[1]) in theSet:
                    check += 1
                else:
                    break
            if check == 3:
                return True
            
            if currPosition in diagonals:
                check = 0 
                for num in range(3):
                    if (num,num) in theSet:
                        check += 1
                    else:
                        break
                if check == 3:
                    return True
                
                check = 0
                if (0,2) in theSet and (1,1) in theSet and (2,0) in theSet:
                    return True
                
            return False

            
        for i in range(1, n):
            currMove = (moves[i][0], moves[i][1])
            if i % 2 == 0:
                As.add(currMove)
                if len(As) >= 3:
                    if checkForWinner(currMove, As):
                        return "A"


            else:
                Bs.add(currMove)
                if len(Bs) >= 3:
                    if checkForWinner(currMove, Bs):
                        return "B"
        
        if len(As) + len(Bs) == 9:
            return "Draw"
        return "Pending"

