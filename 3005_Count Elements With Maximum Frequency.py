class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        
        maxNum = max(dict.values())
        count = 0
        for key,value in dict.items():
            if value == maxNum:
                count += maxNum
        
        return count


        