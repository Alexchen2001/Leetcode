class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def doDividing(divisorNum):
            sumNum = 0
            for i in nums:
                sumNum += (ceil(i / divisorNum))
            
            if sumNum <= threshold:
                return True
            return False
        
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2

            if doDividing(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


        