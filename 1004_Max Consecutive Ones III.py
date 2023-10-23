class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ## initiates left index pointer
        ## current window zero counter
        ## a place for answer
        left = currZCount = ans = 0
        
        for right in range (len(nums)):
            
            ## checks in the window wheteher if there is 0
            ## if there is inveremet the count of 0s
            if (nums[right] == 0):
                currZCount += 1
            
            ## only occurs is the amt of 0s exceeded threshold k
            ## and moves the window to the right until the 0s
            ## is below the threshold
            while (currZCount > k):
                if (nums[left] == 0):
                    currZCount -= 1
                left += 1
            ## checks whether if there are greater 1s sequence
            ## or the current window is the greates
            ans = max(ans, right - left +1)
            
        return ans