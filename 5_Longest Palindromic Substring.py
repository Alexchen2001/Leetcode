class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        res = ""
        resLen = -1

        for i in range(sLen):
            l,r = i, i + 1
            while l >=0 and r < sLen and s[l] == s[r]:
                tempLen = r - l + 1
                if tempLen > resLen:
                    res = s[l:r + 1]
                    resLen = tempLen
                l -= 1
                r += 1

            l, r = i ,i 
            while l >= 0 and r < sLen and s[l] == s[r]:
                tempLen = r - l + 1
                if tempLen > resLen:
                    res = s[l:r + 1]
                    resLen = tempLen
                l -= 1
                r += 1
        return res

