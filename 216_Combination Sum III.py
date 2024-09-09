class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(index,currSum,currArr):
            if currSum == n and len(currArr) == k:
                res.append(currArr[:])
                return

            if len(currArr) > k:
                return
            
            for i in range(index, 10):
                if currSum + i <= n:
                    currArr.append(i)
                    backtrack(i + 1, currSum + i,currArr)
                    currArr.pop()
        backtrack(1,0,[])
        return res
        

            
