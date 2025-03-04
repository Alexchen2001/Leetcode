class Solution:
    def search(self, nums: List[int], target: int) -> int:
        initial = nums[0]
        n = len(nums)
        pivot = n -1
        low, high = 0, n -1
        if nums[0] > nums[n - 1]:
            while low <= high:
                mid = (low + high) // 2
                print(low, high, mid, nums[mid])
                if nums[mid] > nums[mid + 1]:
                    pivot = mid
                    break
                elif nums[mid] >= initial:
                    low = mid + 1
                else:
                    high = mid - 1
        print(pivot)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            realIndex = (mid + pivot + 1) % n
            if nums[realIndex] == target:
                return realIndex
            elif nums[realIndex] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        