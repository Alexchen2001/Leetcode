class Solution:
    def minSwaps(self, s: str) -> int:
        totalZero = 0
        totalOne = 0
        n = len(s)

        for i in range(n):
            if s[i] == "0":
                totalOne += 1
            else:
                totalZero += 1
        
        if abs(totalZero - totalOne) >1 :
            return -1
        
        def swapCount(startNum):
            swaps = 0
            for currChar in s:
                if currChar != startNum:
                    swaps += 1
                
                if startNum == "1":
                    startNum = "0"
                else:
                    startNum = "1"
            return swaps // 2
        
        swapOne = swapCount("0")
        swapZero = swapCount("1")

        if n % 2 == 0:
            return min(swapOne, swapZero)
        
        if totalOne < totalZero:
            return swapZero
        return swapOne
