class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        dictF = {
            "v":[0,0],  # [N,S]
            "h":[0,0]  # [E,W]
        }

        maxMd = 0
        for ltr in s:
            if ltr == "N":
                dictF["v"][0] += 1
            elif ltr == "S":
                dictF["v"][1] += 1
            elif ltr == "E": 
                dictF["h"][1] += 1
            else:
                dictF["h"][0] += 1
            
            tempBig = max(dictF["v"][0],dictF["v"][1]) + max(dictF["h"][0],dictF["h"][1])
            tempSmall = min(dictF["v"][0],dictF["v"][1]) + min(dictF["h"][0],dictF["h"][1])
            maxMd = max(maxMd,(tempBig - tempSmall) + (2 * min(k,tempSmall)))

        return maxMd
            
