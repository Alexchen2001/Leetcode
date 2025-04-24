from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        maxGroup = -1
        dictF = defaultdict(int)
        res = 0
        for i in range(1, n + 1):
            tempSum = 0
            currNum = str(i)
            for currIdx in currNum:
                tempSum += int(currIdx)
            dictF[tempSum] += 1
            if dictF[tempSum] > maxGroup:
                maxGroup = dictF[tempSum]
                res = 0
            if dictF[tempSum] == maxGroup:
                res += 1
        
        return res


            

