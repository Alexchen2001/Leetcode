class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freqDict = {}
        visited = set()
        for num in nums:
            if num <= k:
                if num not in freqDict:
                    freqDict[num] = 1
                else:
                    freqDict[num] += 1
        
        res = 0
        for key, frequency in freqDict.items():
            compliment = k - key
            if compliment in freqDict:
                if key not in visited and compliment not in visited:
                    visited.add(key)
                    visited.add(compliment)
                    if key != compliment:
                        res += min(frequency, freqDict[compliment])
                    else: 
                        res += frequency // 2

            else:
                visited.add(key)
        return res