class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highestRes = 0
        sum = 0

        for i in gain:
            sum += i
            highestRes = max(highestRes, sum)
        
        return highestRes