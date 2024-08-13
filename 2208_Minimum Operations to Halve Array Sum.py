from heapq import *
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        nums = [- num for num in nums]
        heapify(nums)
        currSum = abs(sum(nums))
        iteration = 0

        while currSum > target:
            iteration += 1
            maxNum = heappop(nums)
            currSum = currSum + (maxNum / 2)
            heappush(nums, maxNum / 2)
        
        return iteration



        