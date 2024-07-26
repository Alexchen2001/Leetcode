class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(currX,currY,counter,visited):
            nonlocal board
            nonlocal word
            if counter < len(word) and counter >= 0:
                if (currX,currY) not in visited and board[currY][currX] == word[counter]:
                    if counter == len(word) - 1:
                        return True
                    # go left
                    visited.add((currX,currY))
                    if currX > 0:
                        if search(currX - 1, currY, counter + 1,visited):
                            return True
                    
                    # go right
                    if currX < len(board[0]) - 1: 
                        if search(currX + 1, currY,counter + 1,visited):
                            return True
                    
                    # go up
                    if currY > 0:
                        if search(currX, currY -1 , counter + 1,visited): 
                            return True

                    #go down
                    if currY < len(board) - 1: 
                        if search(currX, currY + 1,counter + 1,visited):
                            return True
                    visited.remove((currX, currY))
            return False


        for i in range (len(board[0])):
            for j in range(len(board)):
                print("NExt iteration")
                if search(i,j,0,set()) == True:
                    return True
                print()
                print()
                print()
            
            
                
                

        