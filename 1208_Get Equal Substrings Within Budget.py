class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        alphabet_dict = {'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90}
        currCost = 0
        res= 0
        start = 0

        for end in range (len(s)):
            currCost += abs(alphabet_dict[s[end]] - alphabet_dict[t[end]])

            while currCost > maxCost:
                currCost -= abs(alphabet_dict[s[start]] - alphabet_dict[t[start]])
                start += 1
            
            res = max(res, end - start + 1)

       

        return res





        