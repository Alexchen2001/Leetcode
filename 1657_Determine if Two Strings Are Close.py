class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        if n != m:
            return False
        word1Dict = {}
        word2Dict = {}

        for i in range(n):
            if word1[i] not in word1Dict:
                word1Dict[word1[i]] = 1
            else:
                word1Dict[word1[i]] += 1
        
        for j in range(m):
            if word2[j] not in word2Dict:
                word2Dict[word2[j]] = 1
            else:
                word2Dict[word2[j]] += 1

        if set(word1Dict.keys()) != set(word2Dict.keys()):
            return False
        
        if sorted(word1Dict.values()) != sorted(word2Dict.values()):
            return False
        
        return True
            


