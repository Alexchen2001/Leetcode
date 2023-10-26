class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ## obtain alphabet
        alphabet = list(string.ascii_lowercase)
        ## create a set
        visit = set()
        
        ## add all alphabet that we see in the sentence 
        for i in range (len(sentence)):
            visit.add((sentence[i]))
        ## checks if any alphabet is not seen in the sentence
        for i in alphabet:
            if i not in visit:
                return False
        return True