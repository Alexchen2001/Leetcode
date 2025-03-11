class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        dictF = {}
        start = 0
        
        res = 0
        for i in range(k):
            if s[i] not in dictF:
                dictF[s[i]] = 1
            else:
                dictF[s[i]] += 1
            
        if max(dictF.values()) == 1:
            res += 1
        
        for i in range(k -1, n - 1):
            leftLtr = s[start]
            start += 1
            nextLtr = s[i + 1]
            dictF[leftLtr] -= 1

            if nextLtr not in dictF:
                dictF[nextLtr] = 1
            else:
                dictF[nextLtr] += 1
            if max(dictF.values()) == 1:
                res += 1
        return res


