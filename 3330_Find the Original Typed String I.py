class Solution:
    def possibleStringCount(self, word: str) -> int:
        dictF = {}
        prev = ""
        count = 0
        for ltr in word:
            if ltr not in dictF:
                dictF[ltr] = 1
            else:
                if prev == ltr:
                    count += 1
                dictF[ltr] += 1
            prev = ltr
        return count + 1
            

