class Solution:
    def countElements(self, arr: List[int]) -> int:
        ## put the input into a set
        exist = set(arr)
        count = 0
        
        ## if the +1 num in not in the input array then do not count
        for i in range(len(arr)):
            if (arr[i] + 1 in exist):
                count += 1
        
        return count
        