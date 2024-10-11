class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        if n <= 1:
            return n
        leftToRight = [1] * n
        rightToLeft = [1] * n

        # If the element is larger than the prevElement it has to have more canides
        #than prevElement
        for i in range(1,n):
            if ratings[i] > ratings[i -1]:
                leftToRight[i] = leftToRight[i - 1] + 1
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                rightToLeft[j] = rightToLeft[j + 1] + 1
        sum = 0
        for k in range(n):
            sum += max(leftToRight[k], rightToLeft[k])
        
        return sum

