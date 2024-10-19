class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = dividend / divisor
        quotient = int(quotient)
        if quotient < -2**31:
            return -2**31
        elif quotient > 2**31 - 1:
            return 2**31 - 1
        else:
            return quotient