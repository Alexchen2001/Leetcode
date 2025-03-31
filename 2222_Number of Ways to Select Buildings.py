
class Solution:
    def numberOfWays(self, s: str) -> int:
        n0, n1= 0, 0
        n01,n10 = 0,0
        n010,n101 = 0, 0

        for currNum in s:
            if currNum == "1":
                n1 += 1
                n01 += n0
                n101 += n10
            else:
                n0 += 1
                n10 += n1
                n010 += n01
        return n101 + n010
