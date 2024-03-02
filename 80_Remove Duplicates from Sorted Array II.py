class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## since it is only 2, it doesn't need to be checked
        ## base case
        if len(nums) <= 2:
            return len(nums)
        
        ## start with index 2
        res = 2
        for i in range (2,len(nums)):
            '''
            The res stays at the place that needs to be change, and i keeps incrementing
            until if finds a value that is not eqqual to res - 2
            '''
            if nums[i] != nums[res -2]:
                nums[res] = nums[i]
                res += 1
        return res