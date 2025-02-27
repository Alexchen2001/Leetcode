class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        pivotIndex = None
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                pivotIndex = i
                break
        newNums = nums[pivotIndex:] + nums[:pivotIndex]
        for i in range(1, n):
            if newNums[i - 1] > newNums[i]:
                return False
        return True