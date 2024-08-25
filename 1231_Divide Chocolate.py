class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def letsSplit(sweetLevel):
            currSweetLevel = 0
            cutsDone = 1
            for sweet in sweetness:
                currSweetLevel += sweet
                if currSweetLevel >= sweetLevel:
                    cutsDone += 1
                    currSweetLevel = 0
            if cutsDone <= k + 1:
                return True
            return False

        left, right = 0, sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            if letsSplit(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right