class Solution:
    def intToRoman(self, num: int) -> str:
        intDict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        subtractiveDict = {900: 'CM', 400: 'CD', 90: 'XC', 40: 'XL', 9: 'IX', 4: 'IV'}
        res = []
        n = len(str(num))
        pointer = 0

        while num > 0:
            if num >= 1000:
                res.append('M' * (num // 1000))
                num %= 1000
            elif num >= 900:
                res.append('CM')
                num -= 900
            elif num >= 500:
                res.append('D')
                num -= 500
            elif num >= 400:
                res.append('CD')
                num -= 400
            elif num >= 100:
                res.append('C' * (num // 100))
                num %= 100
            elif num >= 90:
                res.append('XC')
                num -= 90
            elif num >= 50:
                res.append('L')
                num -= 50
            elif num >= 40:
                res.append('XL')
                num -= 40
            elif num >= 10:
                res.append('X' * (num // 10))
                num %= 10
            elif num == 9:
                res.append('IX')
                num -= 9
            elif num >= 5:
                res.append('V')
                num -= 5
            elif num == 4:
                res.append('IV')
                num -= 4
            else:
                res.append('I' * num)
                num = 0

        return ''.join(res)
