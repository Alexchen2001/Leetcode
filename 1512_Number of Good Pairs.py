class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res += 1
        return res

        