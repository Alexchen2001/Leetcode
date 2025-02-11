class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        def backtrack(index):
            if index == len(s):
                res.append(" ".join(curArr))
                return 
            for j in range(index, len(s)):
                currS = s[index: j + 1]
                if currS in wordDict:
                    curArr.append(currS)
                    backtrack(j + 1)
                    curArr.pop()
                
        curArr = []
        res = []
        backtrack(0)
        return res

