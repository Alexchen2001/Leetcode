class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        currMax = 0
        health = 1
        for healthDeduction in damage:
            health += healthDeduction
            currMax = max(currMax, healthDeduction)
        currMax = min(armor,currMax)

        health -= currMax
        return health