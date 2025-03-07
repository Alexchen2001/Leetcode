class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [False] * right
        arr[0] = True
        for i in range(2, floor(sqrt(right)) + 1):
            temp = i
            while True:
                temp += i
                if temp <= right:
                    arr[temp - 1] = True
                else:
                    break
        res = [-1, -1]
        prev = -1
        minDiff = 99999999
        for num in range(left, right + 1):
            if arr[num -1] == False:
                if prev == -1:
                    prev = num
                else:
                    currDiff = num - prev
                    if currDiff < minDiff:
                        res[0] = prev
                        res[1] = num
                        minDiff = currDiff
                    prev = num
        return res
            
            
        

