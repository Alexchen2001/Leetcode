class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(currArr,currIndex):
            if len(currArr) == k:
                ans.append(currArr[:])
                return
            
            for i in range(currIndex, n + 1):
                currArr.append(i)
                backtrack(currArr, i + 1)
                currArr.pop()
        backtrack([],1)
        return ans
        