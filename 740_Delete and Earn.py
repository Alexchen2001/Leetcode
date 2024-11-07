from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxNum = -1
        for num in nums:
            if num > maxNum:
                maxNum = num
            freq[num] += num

        points = [0] * (maxNum + 1)
        
        if 1 in freq:
            points[1] = freq[1]
        
        for i in range(2, maxNum + 1):
            points[i] = max(points[i-1], points[i-2] + freq[i])
        
        return points[-1]



        