class Solution:
    def reverse(self, x: int) -> int:
        def inRange(n):
            min32Bit = -2**31
            max32Bit = 2**31 - 1
            return min32Bit <= n <= max32Bit
        if x < 0:
            x = str(x)[0] + str(x)[1::][::-1]
        else:
            x = str(x)[::-1]
        temp = int(x)
        if inRange(temp):
            return temp
        else:
            return 0
