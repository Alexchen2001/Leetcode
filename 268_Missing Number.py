class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## type change the nums into a set
        visit = set(nums)
        
        ## checks whether if we have the 0 to n in the given nums list
        for i in range (len(nums) + 1):
            if i in visit:
                continue
            else:
                return i
        
        