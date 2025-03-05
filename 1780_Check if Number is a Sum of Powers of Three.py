class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        threes = [3** i for i in range(16, -1, -1)]

        for i in range(17):
            print(threes[i])
            if n >= threes[i]:
                n -= threes[i]
            if n == 0 :
                return True
        return False