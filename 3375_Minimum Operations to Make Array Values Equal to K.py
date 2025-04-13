from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        dictF = defaultdict(int)

        for num in nums:
            if num < k:
                return -1
            dictF[num] += 1
        if k in dictF:
            return len(dictF) - 1
        return len(dictF)

        
        
        
        