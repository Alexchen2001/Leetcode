class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ## initiate intial sum whihc is the first value of the array
        runningSum = [nums[0]]
        for i in range (1,len(nums) ):
            ## appends into the array with the addition of previous sum, to achieve 
            ## sum to its current position. 
            runningSum.append(runningSum[-1] + nums[i])
        return runningSum
    