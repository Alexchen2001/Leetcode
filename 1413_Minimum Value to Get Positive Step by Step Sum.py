class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ## initiates a prefix sum array
        prefix = [nums[0]]
        
        ## appending the prefix sum
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
       
        ## for this problem, it wants the min Pos Value, 
        ## so the min Pos Value that not result zero is theh
        ##min number (negative usuualy) + 1, so at min in the 
        ##sum it will result 1
        if (any(j < 0 for j in prefix)):
            ans = abs(min(prefix)) + 1
        else: 
            ans = 1
        
        return ans
        