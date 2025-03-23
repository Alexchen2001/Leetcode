class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        arr = [0,3]
        temp = 4
        for _ in range(20):
            temp *= 4
            arr.append(temp - 1)
        totalAmt = 0
        for (l,r) in queries:
            temp = 0
            for times in range(len(arr)):
                if l > r:
                    break
                else:
                    if l <= arr[times]:
                        nums = min(r,arr[times]) - l + 1
                        temp += (nums * times)
                        l = min(r, arr[times]) + 1
            totalAmt+= math.ceil(temp/ 2)
        
        return totalAmt



