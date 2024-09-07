class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(currArr, index):
            if len(currArr) > index:
                return 
            ans.append(currArr[:])
            for i in range(index, len(nums)):
                currArr.append(nums[i])
                backtrack(currArr, i + 1)
                currArr.pop()




        backtrack([],0)
        return ans

        

