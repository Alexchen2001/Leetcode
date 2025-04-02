class Solution:
    def minimumKeypresses(self, s: str) -> int:
        dictF = {}

        for currLtr in s:
            if currLtr not in dictF:
                dictF[currLtr] = 1
            else:
                dictF[currLtr] += 1
        press = 1
        res = 0
        currNine = 1
        arr = [(ltr,count) for ltr, count in dictF.items()]
        arr.sort(key = lambda x: -x[1])

        for ltr, freq in arr:

            if currNine > 9:
                currNine = 1
                press += 1
            
            res += (press * freq)
            currNine += 1
        return res
        