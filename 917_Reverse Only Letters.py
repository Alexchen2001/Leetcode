class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = list(s)
        lw = 0
        hi = len(ans) -1

        ## two pointer consider every possible case of not being alphabet
        while (lw < hi):
            if (ans[lw].isalpha() and ans[hi].isalpha()):
                    ans[lw], ans[hi] = ans[hi], ans[lw]
                    lw += 1
                    hi -= 1
            elif (not ans[hi].isalpha() and not ans[lw].isalpha()):
                lw +=1
                hi -=1
            elif( ans[hi].isalpha() and not ans[lw].isalpha()):
                lw +=1
            elif(not ans[hi].isalpha() and ans[lw].isalpha()):
                hi -= 1
            else:
                break
        return ''.join(ans)