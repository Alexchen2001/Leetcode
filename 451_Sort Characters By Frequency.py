class Solution:
    def frequencySort(self, s: str) -> str:
        
        dict = {}
        for ltr in range(len(s)):
            if s[ltr] not in dict:
                dict[s[ltr]] = 1
            else:
                dict[s[ltr]] += 1
        
        sorted_dict_desc = [key * value for key, value in sorted(dict.items(), key = lambda item : item[1], reverse = True)]
        return ''.join(sorted_dict_desc)