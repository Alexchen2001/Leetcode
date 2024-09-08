class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digitDir = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans = []

        def backtrack(currStr, currNum):
            if len(currStr) == len(digits):
                ans.append(''.join(currStr))
                return
            

            for ltr in digitDir[digits[currNum]]:
                currStr.append(ltr)
                backtrack(currStr, currNum + 1)
                currStr.pop()
            
        backtrack([], 0)
        return ans

        