class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        resCount = 0

        def checkSym(givenInt):
            currIntStr = str(givenInt)
            n = len(currIntStr)
            if n % 2 == 1:
                return False
            start = 0
            end = n - 1
            totalL = 0
            totalR = 0
            while start < end:
                totalL += int(currIntStr[start])
                totalR += int(currIntStr[end])
                start += 1
                end -= 1
            if totalL != totalR:
                return False
            return True
        
        for i in range(low, high + 1):
            if checkSym(i):
                resCount += 1
        return resCount
                




