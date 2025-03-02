class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        newArr = []
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > 0:
                if nums[i] == nums[i + 1]:
                    nums[i] = nums[i] + nums[i]
                    nums[i + 1] = 0
                newArr.append(nums[i])
        if nums[n -1] > 0:
            newArr.append(nums[n -1])
        zeros = n - len(newArr)
        newArr.extend([0] * zeros)
        return newArr
