class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort
        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            
            mid = n // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)

        

        def merge(leftArr, rightArr):
            lIndex, rIndex= 0, 0
            nL, nR = len(leftArr), len(rightArr)
            merged = []

            while lIndex < nL and rIndex < nR:
                if leftArr[lIndex] <= rightArr[rIndex]:
                    merged.append(leftArr[lIndex])
                    lIndex += 1
                else:
                    merged.append(rightArr[rIndex])
                    rIndex += 1
            merged.extend(leftArr[lIndex:])
            merged.extend(rightArr[rIndex:])

            return merged
        return mergeSort(nums)


