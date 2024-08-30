class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        i, j = 0, sum(nums)
        
        for k in range (len(nums)):
            j -= nums[k]
            if i == j:
                return k
            i += nums[k]
        
        return -1
            
            

        