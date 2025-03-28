class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ltrLog = []
        digLog = []
        n = len(logs)
        for logIndex in range(n):
            identifier, *rest= logs[logIndex].split(" ")
            
            if rest[0].isdigit():
                digLog.append(logs[logIndex])
            else:
                # (content,identifier, index)
                ltrLog.append((" ".join(rest),identifier,logIndex))
        ltrLog.sort(key = lambda x: (x[0],x[1]))

        print(ltrLog)
        res = []
        for ltrL in ltrLog:
            res.append(logs[ltrL[2]])
        
        return res + digLog

