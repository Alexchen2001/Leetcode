class Solution:
    def jump(self, nums: List[int]) -> int:
        currEndPoint = 0
        furthestPoint = 0
        res = 0
        n = len(nums)

        for i in range(n - 1):
            furthestPoint = max(furthestPoint, i + nums[i])
            
            if i == currEndPoint:
                res += 1
                currEndPoint = furthestPoint
        return res


        