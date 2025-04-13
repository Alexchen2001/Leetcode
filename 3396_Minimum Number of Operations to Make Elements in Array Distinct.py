from collections import defaultdict
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dictF = defaultdict(int)
        duplicated = set()
        n = len(nums)
        for num in nums:
            dictF[num] += 1
            if dictF[num] > 1:
                duplicated.add(num)
        if len(duplicated) < 1:
            return 0
        start = 0
        count = 0
        while start < n:

            for i in range(start, min(start + 3, n)):
                dictF[nums[i]] -= 1
                if dictF[nums[i]] < 2 and nums[i] in duplicated:
                    duplicated.remove(nums[i])
            count += 1
            start += 3
            if len(duplicated) < 1:
                return count
        return count


        
