class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxLen = 0
        n = len(nums)
        currLen = 0
        zeroIgnored = False
        deleteEver = False

        while left <= right and right < n:

            if nums[right] == 1:
                currLen += 1
                if currLen > maxLen:
                    maxLen = currLen
                right += 1
            elif nums[right] == 0 and not zeroIgnored:
                right += 1
                zeroIgnored = True
                deleteEver = True
            elif nums[right] == 0 and zeroIgnored:
                while nums[left] != 0:
                    left += 1
                    currLen -= 1
                left += 1
                zeroIgnored = False
        if deleteEver:
            return maxLen
        else:
            return maxLen -1
            

            
