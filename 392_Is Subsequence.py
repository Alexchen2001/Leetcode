class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        txt1 = 0
        txt2 = 0
        m = len(s)
        n = len(t)
        if m > n:
            return False

        while txt2 <= n:
            print(txt1)
            print(txt2)
            if txt1 >= m:
                return True
            elif txt2 >= n:
                return False
            elif s[txt1] == t[txt2]:
                txt1 += 1
                txt2 += 1
            else:
                txt2 += 1
        return False
            
