class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(startIndex, aim, currArr):
            if aim == 0:
                res.append(currArr[:])
                return
            

            for i in range(startIndex, n):
                if aim - candidates[i] >= 0:
                    currArr.append(candidates[i])
                    backtrack(i, aim - candidates[i], currArr)
                    currArr.pop()
        backtrack(0, target, [])
        return res
