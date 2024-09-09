class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def isValid(x,y, givenArr):
            for (setX, setY) in givenArr:
                if setX == x or setY == y:
                    return False
                if abs(setX - x) == abs(setY - y):
                    return False
            return True
        
        def backtrack(startX,currArr):
            nonlocal res
            if len(currArr) == n:
                res += 1
                return
        
            for j in range(n):
                if isValid(startX,j, currArr):
                    currArr.append((startX,j))
                    backtrack(startX + 1, currArr)
                    currArr.pop()
        backtrack(0,[])
        return res

            

        

