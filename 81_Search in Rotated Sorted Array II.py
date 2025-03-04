class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        pivot = n-1

        for i in range(n -1):
            if nums[i] > nums[i + 1] :
                pivot = i
                break
        low = 0
        high = n - 1
        print(pivot)
        while low <= high:
            mid = (low + high) // 2
            realIndex = (mid + pivot +1) % n
            print(low, high, realIndex, nums[realIndex])
            if nums[realIndex] == target:
                return True
            elif nums[realIndex] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        