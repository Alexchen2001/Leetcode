class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        referenceP= {}
        referenceS = {}
        s = s.split()
        n = len(pattern)
        m = len(s)

        if m != n:
            return False
        for i in range(n):
            
            if pattern[i] not in referenceP and s[i] not in referenceS:
                referenceP[pattern[i]] = s[i]
                referenceS[s[i]] = pattern[i]
            else:
                if pattern[i] in referenceP:
                    if referenceP[pattern[i]] != s[i]:
                        return False
                if s[i] in referenceS:
                    if referenceS[s[i]] != pattern[i]:
                        return False
        return True



                