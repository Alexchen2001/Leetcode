class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        res = -1
        while True:
            if len(nums) == 1:
                return nums[0]
            n = len(nums)
            temp = []
            for i in range(n - 1):
                temp.append((nums[i] + nums[i + 1]) % 10)
            


            if len(temp) <= 1:
                res = temp[0]
                break
            nums = temp
        return res



