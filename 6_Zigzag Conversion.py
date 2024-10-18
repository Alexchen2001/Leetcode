class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [""] * numRows
        n = len(s)
        endPivotIndex = numRows - 2
        startPivotIndex = 1
        index = 0
        rIndex = 0
        while index < n:
            while rIndex < numRows and index < n:
                arr[rIndex] = arr[rIndex] + s[index]
                rIndex += 1
                index += 1
            rIndex = endPivotIndex
            while rIndex >= startPivotIndex and index < n:
                arr[rIndex] = arr[rIndex] + s[index]
                rIndex -= 1
                index += 1
        return ''.join(arr)
            
                





