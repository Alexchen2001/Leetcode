class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        sum = 0
        res = 0
        for apple in weight:
            sum += apple
            if sum > 5000:
                return res
            res += 1
        
        return res
        