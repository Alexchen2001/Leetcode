class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arrL = []
        arrM = []
        arrR = []

        for num in nums:
            if num == pivot:
                arrM.append(num)
            elif num < pivot:
                arrL.append(num)
            else:
                arrR.append(num)
        res = arrL + arrM + arrR
        return res