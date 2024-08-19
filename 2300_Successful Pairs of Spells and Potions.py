class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        res = []
        
        def returnValidAmt(target):
            nonlocal potions
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return len(potions) - left
        for i in spells:
            res.append(returnValidAmt(success / i))
        
        return res


