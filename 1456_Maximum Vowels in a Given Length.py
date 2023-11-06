class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ## puts the vowels in the set 
        vowels = set('aeiouAEIOU')
        ## sliding window
        lw = 0
        hi = k - 1
        prev = 0
        result = 0
        ## initial run through 
        for i in range(k):
            if s[lw+i] in vowels:
                prev += 1
                result = prev
        ## checks the previous character that was exclude and newly
        ## included character for vowels, increment/dcrement the amount of the 
        ## vowels in the interval accordingly.
        while (True):
            lw +=1 
            hi += 1

            if (hi == len(s)):
                break
            
            if (s[lw -1] in vowels):
                prev -= 1
            if (s[hi] in vowels):
                prev +=1
            
            if (prev > result):
                result = prev
        
        return result
            


