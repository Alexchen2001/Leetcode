class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        maxTripVal = 0
        diff = 0 
        greatestVal = nums[0]

        for i in range(1, n):
            maxTripVal = max(maxTripVal, diff * nums[i])
            diff = max(diff, greatestVal - nums[i])
            greatestVal = max(greatestVal, nums[i])

        return maxTripVal



