class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = set()
        dictF = {} # dictF[word] = (ltrFreq, wordcount)

        for word in strs:
            ltrFreq = {}
            if word in dictF:
                dictF[word][1] += 1
            else:
                for ltr in word:
                    if ltr not in ltrFreq:
                        ltrFreq[ltr] = 1
                    else:
                        ltrFreq[ltr] += 1

                dictF[word] = [ltrFreq,1]
                visited.add(word)

        
        res = []
        n = len(strs)
        for i in range(n):
            if strs[i] in visited:
                tempArr = []
                for j in range(i + 1,n):
                    if strs[j] in visited:
                        if len(strs[i]) == len(strs[j]):
                            if strs[i] != strs[j]:
                                if dictF[strs[i]][0] == dictF[strs[j]][0]:
                                    for _ in range(dictF[strs[j]][1]):
                                        tempArr.append(strs[j])
                                    dictF.pop(strs[j])
                                    visited.remove(strs[j])
            
                for _ in range(dictF[strs[i]][1]):
                    tempArr.append(strs[i])
                dictF.pop(strs[i])
                visited.remove(strs[i])
                res.append(tempArr)
        
        return res
            
                        

                        





