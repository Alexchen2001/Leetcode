import heapq
from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dictF = defaultdict(int)
        maxQ = []
        res = []
        
        for i in range(min(k,n)):
            dictF[nums[i]] += 1
            heappush(maxQ, -1 * nums[i])
        
        currMax = -1 * heappop(maxQ)
        res.append(currMax)
        dictF[currMax] -= 1
        if nums[0] != currMax:
            dictF[nums[0]] -= 1
            if dictF[nums[0]] <= 0:
                dictF.pop(nums[0])
            heappush(maxQ, -1 * currMax)
            dictF[currMax] += 1
        else:
            if dictF[nums[0]] <= 0:
                dictF.pop(nums[0])

        prev = 1
        for i in range(k,n):
            dictF[nums[i]] += 1
            heappush(maxQ, -1 * nums[i])

            currMax = -1 * heappop(maxQ)
            while currMax not in dictF:
                currMax = -1 * heappop(maxQ)
            res.append(currMax)
            dictF[currMax] -= 1
            if nums[prev] != currMax:
                dictF[nums[prev]] -= 1
                if dictF[nums[prev]] <= 0:
                    dictF.pop(nums[prev])
                heappush(maxQ, -1 * currMax)
                dictF[currMax] += 1
            else:
                if dictF[nums[prev]] <= 0:
                    dictF.pop(nums[prev])

            prev += 1
        print(res)
        return res