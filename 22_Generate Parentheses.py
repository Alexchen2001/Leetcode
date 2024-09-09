class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(lefty, righty, currArr):

            if lefty == n and righty == n:
                res.append(''.join(currArr))
                return 

            if lefty < n:
                currArr.append('(')
                backtrack(lefty + 1, righty, currArr)
                currArr.pop()
            
            if righty < lefty :
                currArr.append(')')
                backtrack(lefty, righty + 1, currArr)
                currArr.pop()
        backtrack(0,0,[])
        return res
            
            

        