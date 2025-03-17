class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 1:
            return False
        dictF = {}

        for num in nums:
            if num not in dictF:
                dictF[num] = 1
            else:
                dictF[num] += 1
        for key,value in dictF.items():
            if value % 2 == 1:
                return False
        return True