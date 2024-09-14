class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        maxLength = 0
        for num in arr:
            compliment = num - difference

            if compliment in dp:
                dp[num] = dp[compliment] + 1
            else:
                dp[num] = 1
            maxLength = max(maxLength, dp[num])
        return maxLength
