from itertools import combinations
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        n = len(nums)
        def check(possibleDistance):
            validPairCount = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= possibleDistance:
                    j+= 1
                # adding all the possible pair between (i,j) excluding (i,j) and (i,i)
                validPairCount += (j - i - 1)
            return validPairCount
        
        while low < high:
            mid = (low + high) // 2

            if check(mid) < k:
                low = mid + 1
            else:
                high = mid
        return high
