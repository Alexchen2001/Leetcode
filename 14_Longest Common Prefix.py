class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        n = len(strs)
        for i in range(1, n):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix