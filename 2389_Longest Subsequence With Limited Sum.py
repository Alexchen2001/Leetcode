class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefixSum = [0]* n
        prefixSum[0] = nums[0]
        for i in range(1,n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        ans = []

        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return left

        
        for num in queries:
            ans.append(binarySearch(prefixSum,num))
        
        return ans

