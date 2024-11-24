# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        possibleP = 0
        for i in range(1, n):
            if knows(possibleP, i):
                possibleP = i

        for i in range(n):
            if i != possibleP:
                if knows(possibleP, i) or not knows(i,possibleP):
                    return -1
        return possibleP

        
        