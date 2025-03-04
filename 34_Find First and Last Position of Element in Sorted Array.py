class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        n = len(nums)
        high =n - 1

        def checkL(givenIndex):
            if givenIndex > 0:
                if nums[givenIndex -1] == target:
                    return False
            return True
        def checkR(givenIndex):
            if givenIndex < n - 1:
                if nums[givenIndex +1] == target:
                    return False
            return True
        #finding Left most index target
        res1 = -1
        res2 = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and checkL(mid):
                res1 = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if res1 == -1:
            return [-1,-1]
        
        low = 0
        high = n -1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target and checkR(mid):
                res2 = mid
                break
            elif nums[mid] > target:
                high = mid  - 1
            else:
                low = mid + 1
        return [res1,res2]
        
        
            
                


        