from collections import Counter
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        n = len(people)
        saved = [0] * n 
        i, j = 0 , n -1
        res = 0
        sumNum = 0

        if i == j:
            return 1
        
        while sumNum != n and i < n:
            if saved[i] != 1:
                composite = limit - people[i]
                saved[i] = 1
                sumNum += 1
                if people[j] <= composite and saved[j] != 1:
                    saved[j] = 1
                    sumNum += 1
                    j -= 1
                res += 1
            i += 1

        return res
            
            


        