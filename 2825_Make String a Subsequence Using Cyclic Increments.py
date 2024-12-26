class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alphabet = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}  

        n = len(str1)
        m = len(str2)
        str2i = 0
        for i in range(n):
            if str1[i] == str2[str2i] or str1[i] == alphabet[str2[str2i]]:
                str2i += 1
            
            if str2i >= m:
                return True
        return False

