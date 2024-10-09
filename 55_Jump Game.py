class Solution:
    def canJump(self, nums: List[int]) -> bool:
        GOOD, BAD, UNKNOWN = 1, 0 , -1
        n = len(nums)
        memo = [UNKNOWN] * n
        memo[-1] = GOOD

        for i in range(n - 2, -1 ,-1):
            furthestJump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == GOOD:
                    memo[i] = GOOD
                    break
        return memo[0] == GOOD

    