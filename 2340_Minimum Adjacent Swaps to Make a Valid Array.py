class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0
        minIdx = -1
        maxIdx = -1
        for i in range(n):
            if minIdx == -1 or nums[i] < nums[minIdx]:
                minIdx = i
            
            if maxIdx == -1 or nums[i] >= nums[maxIdx]:
                maxIdx = i
        # Min needs to move to 0, so minIdx is how many swaps to get ot leftmost
        #we want to have max go to right most position which n - 1, so we obtain
        # how many swaps to reach right most by what the place of maxIdx is at
        swaps = minIdx + (n - 1 - maxIdx) 

        if minIdx > maxIdx:
            swaps -= 1
        return swaps
        