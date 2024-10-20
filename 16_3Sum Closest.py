class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        closestSum = float("inf")
        for i in range(n):
            j=i+1
            k=n-1
            while j<k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp - target) < abs(closestSum - target):
                    closestSum = temp
                if temp == target:
                    return target
                if temp < target:
                    j=j+1
                else:
                    k=k-1
        return closestSum
