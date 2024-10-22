class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= n:  # Boundary check to avoid index out of range
                return 0
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if (i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)
            
            dp[i] = res
            return res

        return dfs(0)
