class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        res = [None] * n

        for i in range(n):
            if nums[i] <= n and nums[i] > 0:
                res[nums[i] - 1] = nums[i]
        
        for i in range(n):
            if res[i] is None:
                return i + 1
        return res[-1] + 1
            

            