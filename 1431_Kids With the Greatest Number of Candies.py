class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxNum:
                candies[i] = True
            else:
                candies[i] = False
        return candies
