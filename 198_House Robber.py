class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dpTab = [0] * n

        if n < 2:
            return nums[0]
        else:
            dpTab[0] = nums[0]
            dpTab[1] = max(nums[0], nums[1])
        
        for i in range (2, n):
            dpTab[i] = max(nums[i] + dpTab[i - 2], dpTab[i- 1] )
        
        return dpTab[n - 1]
        

        