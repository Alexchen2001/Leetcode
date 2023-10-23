class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ## Main concept: By finding the max sum of the part of the array, 
        ## it will yield the greates average.
        ## Initiated the first to kth element sum
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            
            ## moves the sliding window by 1 to the right.
            currSum += nums[i] - nums[i-k]
            maxSum = max(currSum, maxSum)
            
            
        return maxSum / k
        