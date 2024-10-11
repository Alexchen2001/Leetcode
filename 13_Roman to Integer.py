class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prevElement = 0
        sum = 0
        for ltr in s:
            val = romanDict[ltr]
            if prevElement < val:
                sum = (sum - prevElement) + (val - prevElement)
            else:
                sum += val
            prevElement = val
        return sum


