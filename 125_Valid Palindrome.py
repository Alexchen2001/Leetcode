class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:

            

            while not s[left].isalpha() and left < right:
                if s[left].isdigit():
                    break
                left += 1
                
            while not s[right].isalpha() and right > left:
                if s[right].isdigit():
                    break
                right -= 1
                
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
        