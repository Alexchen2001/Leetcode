class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ## initiate two pointers for the variable and include the first element for the sum
        lw = 0
        hi = 0
        sum = nums[0]
        result = 9999999
        ## checks with a sliding window, increase low if target met
        ## adds high if target not met. finds the best minimal minSubArrayLen
        ## if not found return 0
        while True:
            if (sum >= target):
                if(result > hi - lw + 1):
                    result = hi - lw + 1
                else:
                    sum = sum - nums[lw]
                    lw += 1   
            else:
                hi += 1
                if hi==len(nums):
                    break
                sum = sum + nums[hi]
        
        if result==9999999:
            result=0

        return result

        

