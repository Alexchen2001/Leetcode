class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        currRes = []
        nums.sort(key = lambda x:[x[0],x[1]])
        start, end = nums[0][0],nums[0][1]
        n = len(nums)

        for i in range(1,n):
            if start <= nums[i][0] and nums[i][0] <= end:
                if nums[i][1] > end:
                    end = nums[i][1]
            else:
                currRes.append((start,end))
                start, end = nums[i][0], nums[i][1]
        currRes.append([start,end])
        res = 0
        for start, end in currRes:
            res += (end - start + 1)
        
        return res