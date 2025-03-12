class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        currPow = 2
        nums = 1
        for i in range(32):
            if n == nums:
                return True
            nums = nums * currPow  
        return False
