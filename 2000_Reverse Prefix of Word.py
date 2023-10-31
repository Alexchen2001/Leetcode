class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ## checks if the substring prefix is in the word 
        if ch not in word:
            return word
        
        Fw = -1
        ## finds the first occurence of the ch prefix in the word
        for i in range(len(word)):
            if word[i] == ch:
                Fw = i
                break
        ## reverse the substring till the first occurrence
        temp = word[:Fw+ 1]
        temp = temp[::-1]

        ## joins the string 
        return temp + word[Fw + 1:]