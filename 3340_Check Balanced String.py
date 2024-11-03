class Solution:
    def isBalanced(self, num: str) -> bool:
        n = len(num)
        oddS = 0
        evenS = 0

        for i in range(n):
            #even
            if (i + 1) % 2 == 0:
                evenS += int(num[i])
            else:
                oddS += int(num[i])
        if evenS == oddS:
            return True
        return False
                
                