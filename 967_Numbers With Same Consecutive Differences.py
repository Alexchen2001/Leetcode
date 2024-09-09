class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def backtrack(previousNum,currArr):
            if len(currArr) == n:
                res.append(int(''.join(currArr)))
                return
            
            if previousNum is not None:
                if previousNum + k < 10:
                    currArr.append(str(previousNum + k))
                    backtrack(previousNum + k, currArr)
                    currArr.pop()
            
                if k != 0 and previousNum - k >= 0 :
                    currArr.append(str(previousNum - k))
                    backtrack(previousNum - k, currArr)
                    currArr.pop()

            if previousNum is None:
                for i in range(1,10):
                    currArr.append(str(i))
                    backtrack(i, currArr)
                    currArr.pop()
        
        backtrack(None, [])
        return res

