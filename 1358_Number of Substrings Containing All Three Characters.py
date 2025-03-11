class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        dictF = {
            "a": 0,
            "b": 0,
            "c": 0
        }
        start = 0
        res = 0
        tempLeft = 0

        for end in range(n):
            currLtr = s[end]
            dictF[currLtr] += 1

            while (min(dictF.values()) >= 1):
                tempLeft += 1
                startWord = s[start]
                dictF[startWord] -= 1
                start += 1
            res += tempLeft
        return res