class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        dict = {}

        
        for right in range(len(nums)):
            if nums[right] not in dict:
                dict[nums[right]] = 1
            else:
                dict[nums[right]] += 1
                while dict[nums[right]] > k and left <= right:
                    dict[nums[left]] -= 1
                    left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength
                
        