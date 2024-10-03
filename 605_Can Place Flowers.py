class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        L = len(flowerbed)

        for i in range(L):

            if flowerbed[i] == 0:
                leftpot = (i == 0) or (flowerbed[i - 1] == 0) 
                rightpot = (i == L - 1) or (flowerbed[i + 1] == 0)


                if leftpot and rightpot:
                    flowerbed[i] = 1
                    n -= 1
        
        if n <= 0:
            return True
        return False

