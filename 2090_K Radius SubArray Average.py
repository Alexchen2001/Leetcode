class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        ## edge case
        if(k == 0):
            return nums
    
        n = len(nums)
        averageArr = [-1] * n
        
        ## if initially the nums do not have enough elements after the  element from left and right
        if (2 * k + 1 > n):
            return averageArr
        
        ## prefix sum for the sum of the array that loops to n
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        
        for i in range (k, n -k):
            ## two pointers
            left, right = i -k, i + k
            ## obtains only the sum within the two pointer range
            subArrSum = prefix[right + 1] - prefix[left]
            ## floor division would not result decimal
            avg = subArrSum // (2 * k + 1)
            averageArr[i] = avg
        return averageArr
        
        