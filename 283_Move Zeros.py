class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lw = 0
        hi = 0
        n = len(nums)
        while(lw < n and hi < n):
            if (nums[lw] == 0):
                if (nums[hi] != 0):
                    nums[lw],nums[hi] = nums[hi], nums[lw]
                else: 
                    hi +=1 
            else: 
                lw += 1
                hi += 1

        