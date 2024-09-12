class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dp(row, col):
            # Base case: if we're at the last row, return the current value
            if row == m - 1:
                return matrix[row][col]
            
            # Recursive case: try moving to the next row in three possible directions
            ans = matrix[row][col]
            best_next_move = float('inf')
            
            # Move directly down
            best_next_move = min(best_next_move, dp(row + 1, col))
            
            # Move diagonally left, if it's within bounds
            if col - 1 >= 0:
                best_next_move = min(best_next_move, dp(row + 1, col - 1))
            
            # Move diagonally right, if it's within bounds
            if col + 1 < n:
                best_next_move = min(best_next_move, dp(row + 1, col + 1))
            
            # Return the current value plus the minimum of the next possible moves
            return ans + best_next_move

        m, n = len(matrix), len(matrix[0])
        res = float('inf')
        
        # Try starting from every column in the first row
        for i in range(n):
            res = min(res, dp(0, i))
        
        return res
