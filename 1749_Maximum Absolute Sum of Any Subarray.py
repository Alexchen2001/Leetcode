class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        currSumMax = nums[0]
        currSumMin = nums[0]
        n = len(nums)

        for i in range(1, n):
            currSumMax = max(nums[i], currSumMax + nums[i])
            currSumMin = min(nums[i], currSumMin + nums[i])
            currMax = max(currSumMax, currMax)
            currMin = min(currSumMin, currMin)


        return max(abs(currMin),abs(currMax))