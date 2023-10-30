from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ## the value of the dictionary has to be "int"
        dictN = defaultdict(int)
        dictM = defaultdict(int)
        
        ## traverses the two string input and create a hashmap of frequency
        for i in ransomNote:
            if i in dictN:
                dictN[i] += 1
            else:
                dictN[i] = 1
                
        for j in magazine:
            if j in dictM:
                dictM[j] += 1
            else:
                dictM[j] = 1
        
        ## decides whether if magazine string has the minimal frequency
        ## reqruied to create ransomNote
        for k in dictN:
            if k not in dictM:
                return False
            elif dictM[k] < dictN[k]:
                return False
            else: 
                continue
        return True
        
                
            
        
        