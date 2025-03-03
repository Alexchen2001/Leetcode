class Solution:
    def mySqrt(self, x: int) -> int:
        start = 1
        end = x // 2

        if x == 0 or x == 1:
            return x
        while start <= end:
            mid = (start + end) // 2
            squared = mid * mid
            if squared == x:
                return mid
            elif squared < x:
                start = mid + 1
            else:
                end = mid - 1
        
        return end