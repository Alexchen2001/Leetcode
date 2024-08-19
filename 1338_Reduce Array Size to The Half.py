from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        originalSize = len(arr)
        counts = Counter(arr)
        counts = sorted([item[1] for item in counts.items()])
        currLength = 0
        res = 0
        for values in counts:
            if currLength + values > originalSize / 2:
                return len(counts) - res
            currLength += values
            res += 1
        return len(counts) - res

