class Solution:
    def findMin(self, nums: List[int]) -> int:

        initial = nums[0]
        n = len(nums)
        pivot = n -1
        low, high = 0, n -1
        if nums[0] > nums[n - 1]:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > nums[mid + 1]:
                    pivot = mid
                    break
                elif nums[mid] >= initial:
                    low = mid + 1
                else:
                    high = mid - 1
        return nums[(pivot + 1) % n]
