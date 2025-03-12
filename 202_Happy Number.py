class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        visited = set()
        while int(n) not in visited and int(n) != 1:
            visited.add(int(n))
            temp = list(n)
            tempStr = 0
            for numStr in temp:
                numStr = int(numStr)
                tempStr += (numStr * numStr)
            n = str(tempStr)

        
        if int(n) == 1:
            return True
        return False