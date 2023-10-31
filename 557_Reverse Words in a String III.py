class Solution:
    def reverseWords(self, s: str) -> str:
        ## splits the word by spaces
        words = s.split()
        ## reverses the word one by one
        reversedW = [word[::-1] for word in words]
        ## provides the answer with joining the empty string with
        ## space
        return ' '.join(reversedW)
        



        