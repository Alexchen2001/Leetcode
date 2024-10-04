class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0
        
        while start < end:
            ValL = height[start]
            ValR = height[end]
            maxArea = max(maxArea, min(ValL,ValR) * (end - start))
            
            if ValL >= ValR:
                end -= 1
            else:
                start += 1
        return maxArea



        