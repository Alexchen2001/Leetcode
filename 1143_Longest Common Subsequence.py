class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(ltr1,ltr2):
            if ltr1 >= len(text1) or ltr2 >= len(text2):
                return 0 
            
            if text1[ltr1] == text2[ltr2]:
                return 1 + dp(ltr1 + 1, ltr2 + 1)
            else:
                return max(dp(ltr1 + 1, ltr2), dp(ltr1, ltr2 + 1))
            
        return dp(0,0)