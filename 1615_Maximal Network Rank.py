from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roadAmt = [0] * n
        directRoad = set()

        for cityA, cityB in roads:
            roadAmt[cityA] += 1
            roadAmt[cityB] += 1
            directRoad.add((cityA, cityB))
            directRoad.add((cityB, cityA))

        maxLength = 0
        for i in range (n):
            for j in range(i + 1,n):
                rank = roadAmt[i] + roadAmt[j]

                if (i,j) in directRoad:
                    rank -= 1
                maxLength = max(maxLength, rank)
        return maxLength
        