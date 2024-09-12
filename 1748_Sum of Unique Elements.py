class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        duplicated = set()
        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = 1
                duplicated.add(num)
            elif num in dict and num in duplicated:
                duplicated.remove(num)
            
                
        
        return sum(duplicated)
        