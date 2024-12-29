class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(num):
            count = 0
            for ball in nums:
                count = count + (math.ceil(ball/num) - 1)
            return count

        high = max(nums)
        low = 1

        while low < high:

            mid = (low + high) // 2

            res = check(mid)

            if res <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return low


            





        

                