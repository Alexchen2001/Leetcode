class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n -1 

        while left <= right:
            mid = (left + right) //2
            row = mid // n # divide by how many element in one row to obtain which row
            column = mid % n # divisible by how many column to find the column
            num = matrix[row][column]

            if num == target: 
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return False