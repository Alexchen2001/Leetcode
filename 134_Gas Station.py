class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGain = 0
        currGain = 0
        answer = 0

        for i in range(len(gas)):
            totalGain += gas[i] - cost[i]
            currGain += gas[i] - cost[i]

            if currGain < 0:
                currGain = 0
                answer = i + 1
        
        if totalGain >= 0:    
            return answer
        return -1