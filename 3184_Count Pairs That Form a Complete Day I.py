class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(len(hours) - 1):
            currVal = hours[i]
            for j in range(i + 1,len(hours)):
                if (currVal + hours[j]) % 24 == 0:
                    count += 1
                       
        return count
        #brute force