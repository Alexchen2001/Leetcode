class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        cost = []
        wizards = len(skill)
        potions = len(mana)
        cost = []
        cost.append(0)
        for wizard in range(wizards):
            cost.append(cost[-1]+ (skill[wizard] * mana[0]))

        finalMatrix = []
        finalMatrix = cost[1::]
        for potion in range(1, potions):
            temp = []
            maxTime = 0
            cost = 0 
            for wizard in range(wizards):
                maxTime = max(finalMatrix[wizard] - cost, maxTime)
                cost = cost + (skill[wizard] * mana[potion])
                temp.append(cost)
                
            for i in range(len(temp)):
                temp[i] = temp[i] + maxTime

            finalMatrix= temp

        return finalMatrix[-1]
        
            
                
                
                

            
                