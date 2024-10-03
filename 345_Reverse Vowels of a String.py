class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i','o','u'}
        s = list(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            
            if s[left].lower() in vowels and s[right].lower() in vowels:
                temp = s[right]
                s[right] = s[left]
                s[left] = temp
                right -= 1
                left += 1
            elif s[left].lower() not in vowels and s[right].lower() in vowels:
                left += 1
            elif s[left].lower() in vowels and s[right].lower() not in vowels:
                right -= 1
            else:
                left += 1
                right -= 1
        
        return ''.join(s)

        