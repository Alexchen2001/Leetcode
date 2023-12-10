class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
        count = 0
        for i in range(len(batteryPercentages)):
            
            if(batteryPercentages[i] > 0):
                count += 1
                if(i == len(batteryPercentages) - 1):
                    break
                for z in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[z] -= 1
            
            
        return count
        