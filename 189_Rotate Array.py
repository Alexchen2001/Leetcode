class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[(i + k) % n] = nums[i]
        
        for j in range(n):
            nums[j] = res[j]
