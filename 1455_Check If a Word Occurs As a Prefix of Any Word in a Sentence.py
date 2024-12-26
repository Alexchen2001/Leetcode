class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(" ")
        n = len(arr)
        wLen = len(searchWord)
        for i in range(n):
            if arr[i][:wLen] == searchWord:
                return i + 1
        return -1