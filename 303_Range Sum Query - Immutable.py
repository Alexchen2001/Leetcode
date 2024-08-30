class NumArray:

    def __init__(self, nums: List[int]):
        self.numArr = [0]

        for i in range(len(nums)):
            self.numArr.append(self.numArr[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        
        rightSum = self.numArr[right + 1]
        leftSum = self.numArr[left ]
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)