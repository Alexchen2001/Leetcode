class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # not all people (except townjudge) trusted someone
        if len(trust) < n -1:
            return -1
        incomingTrust = [0] * (n + 1)
        outgoingTrust = [0] * (n + 1)

        for personX, personY in trust:
            incomingTrust[personY] += 1
            outgoingTrust[personX] += 1
        
        for i in range(1, n + 1):
            if incomingTrust[i] == n -1 and outgoingTrust[i] == 0:
                return i
        return -1

