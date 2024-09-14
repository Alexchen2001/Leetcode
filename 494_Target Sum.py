class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(index, sum):
            if index == n:
                if sum == target:
                    return 1
                return 0
            
            currVal = nums[index]
            subtraction = dp(index + 1, - currVal + sum)
            addition = dp(index + 1, currVal + sum)
            return addition + subtraction

        return dp(0,0)
            

            
            




            
        