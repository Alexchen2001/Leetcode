class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(currArr):
            if len(currArr) == n:
                ans.append(currArr[:])
                return 
            
            for num in nums:
                if num not in currArr:
                    currArr.append(num)
                    backtrack(currArr)
                    currArr.pop()
        
        backtrack([])

        return ans
        