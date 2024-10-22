class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(currSum, maxSum)
        return maxSum