class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        @cache
        def dp(start, end):
            if end == n and s[start:end] in wordDict:
                return True
            if end == n and s[start:end] not in wordDict:
                return False
            
            status = False
            if s[start:end] in wordDict:
                status = status or dp(end, end + 1)
                status = status or dp(start, end + 1)
            else:
                status = status or dp(start, end + 1)
            
            return status 
        
        return dp(0, 1)




        