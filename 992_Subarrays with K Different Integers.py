class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def countK(nums, k):
            dictF = {}
            n = len(nums)
            res = 0
            start = 0

            if k == 0:
                return 0
            

            for end in range(n):
                currLtr = nums[end]

                if currLtr in dictF:
                    dictF[currLtr] += 1
                else:
                    dictF[currLtr] = 1
                
                while len(dictF) > k:
                    leftMost = nums[start]
                    dictF[leftMost] -= 1
                    if dictF[leftMost] <= 0:
                        del dictF[leftMost]
                    start += 1
                res += end - start + 1
                
            return res
        
        return countK(nums,k) - countK(nums,k -1)


        