class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]
        ptrL = 0
        ptrR = len(height) - 1
        rW = 0
        while ptrL < ptrR:

            tempPtr = -1
            if height[ptrL] <= height[ptrR]:
                ptrL += 1
                tempPtr = ptrL
                leftMax = max(leftMax, height[tempPtr])
            else:
                ptrR -= 1
                tempPtr = ptrR
                rightMax = max(rightMax, height[tempPtr])

            currMin = min(leftMax,rightMax)
            if currMin > height[tempPtr]:
                rW += (currMin - height[tempPtr])

        return rW


