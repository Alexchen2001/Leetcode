class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        n = len(digits)
        rem = 0
        for i in range(n - 1, -1, -1):
            if i == n -1:
                temp = digits[i] + 1
                if temp > 9:
                    res.append(temp % 10)
                    rem = temp // 10
                else:
                    res.append(temp)
                    rem = 0
            else:
                temp = digits[i] + rem
                if temp > 9:
                    res.append(temp % 10)
                    rem = temp // 10
                else:
                    res.append(temp)
                    rem = 0
        if rem != 0:
            res.append(rem)
        return res[::-1]


            