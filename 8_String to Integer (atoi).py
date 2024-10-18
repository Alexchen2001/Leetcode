class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        surpass = False
        digitObtained = False
        doneLeadingdigit = False
        for ltr in s:
            if ltr.isdigit():
                surpass = True
                doneLeadingdigit = True
                res = res + ltr
            elif (ltr == "-" or ltr == "+")and not surpass:
                surpass = True
                res = res + ltr
            elif ltr == " " and not surpass:
                continue
            elif not ltr.isdigit():
                break
        if len(res) <= 0:
            return 0
        elif len(res) == 1 and (res[0] == "-" or res[0] == "+") :
            return 0
        else:
            print(res)
            if res[0] == "+":
                res = res[1::]
            res = int(res)
            if res < -2**31:
                return -2**31
            elif res > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(res)
        
            

        