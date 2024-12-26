class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        for i in range(1, n + 1):
            if maxSum < i:
                return count
            if i <= maxSum and i not in banned:
                print(i)
                count += 1
                maxSum -= i
        return count

            