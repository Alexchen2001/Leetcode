class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        while a > 0 or b > 0:
            if a < b and (a >= 1 and b >= 2):
                res = res + (2 * "b") + (1 * "a")
                b = b - 2
                a = a -1


            elif a > b and (b >= 1 and a >= 2):
                res = res + (2 * "a") + (1 * "b")
                b = b - 1
                a = a -2
            elif a == b:
                res = res + "ba"
                a -= 1
                b -= 1

            else:
                if a == 0:
                    res = res + (b *"b")
                    b -= b
                else:
                    res = res + (a * "a")
                    a -= a
        return res