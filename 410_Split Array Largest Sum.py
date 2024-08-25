class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def sumCheck(givenMax):
            sum = 0
            countK = 1
            for item in nums:
                sum += item
                if sum > givenMax:
                    sum = item
                    countK += 1
    
            if countK <= k:
                return True
            return False

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if sumCheck(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

