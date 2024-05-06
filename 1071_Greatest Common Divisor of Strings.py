class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       ## All string should look the same back and forth
       ## when they are divisible
        if str1 + str2 != str2 + str1:
            return ""

        ##The gcd is the greatest number of repeqing pattern 
        ## that could form both strings
        from math import gcd 
        return str1[:gcd(len(str1), len(str2))]

        