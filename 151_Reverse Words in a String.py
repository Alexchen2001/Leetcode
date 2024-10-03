class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ''
        for i in range(len(s) - 1, -1, -1):
            if i == len(s) - 1:
                res = s[i]
            else:
                res = res + ' ' + s[i]
        return res

