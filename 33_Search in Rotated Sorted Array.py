class Solution:
    def search(self, nums: List[int], target: int) -> int:
        prev = nums[0]
        pivot = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < prev:
                pivot = i
                break
        print(pivot)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            realIndex = (mid + pivot) % n
            if nums[realIndex] == target:
                return realIndex
            elif nums[realIndex] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        