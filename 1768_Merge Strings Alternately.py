class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        arr = []

        if m == n:
            for i in range(m):
                arr.append(word1[i])
                arr.append(word2[i])
        elif m > n:
            for i in range(n):
                arr.append(word1[i])
                arr.append(word2[i])
            arr.append(word1[i + 1:])
        else:
            for i in range(m):
                arr.append(word1[i])
                arr.append(word2[i])
            arr.append(word2[i + 1:])
        
        return ''.join(arr)

                