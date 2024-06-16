class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        dictH = {}
        for hour in hours:
            hourCal = hour % 24
            if hourCal not in dictH:
                dictH[hourCal] = 1
            else:
                dictH[hourCal] += 1
        
        for i in range(len(hours) - 1):
            
            dictH[hours[i] % 24 ] -= 1
            
            for num, numCount in dictH.items():
                if (num + hours[i]) % 24 == 0:
                    count += numCount
        return count
            
            