class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if n > ceil(hour):
            return -1 
        def checkTimeS(speed):
            hours = 0
            for i in dist:
                hours = ceil(hours)
                hours += (i / speed)
            
            if hours <= hour:
                return True
            return False

        
        left, right = 1, 10** 7
        while left <= right:
            mid = (left + right) // 2

            if checkTimeS(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        