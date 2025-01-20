
from collections import deque
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        queue = deque([])
        for i in range(n):
            if nums[i] < 0:
                return 0
            if nums[i] > 0:
                queue.append(i)
        
        while queue:
            count += 1
            minNum = min(x for x in nums if x > 0)
            qLen = len(queue)
            for _ in range(qLen):
                index = queue.popleft()
                nums[index] -= minNum
                if nums[index] != 0:
                    queue.append(index)
        return count


        