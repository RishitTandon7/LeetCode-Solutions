from typing import List, Optional

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        
        # Get the number of rows and columns in the grid
        m = len(grid)
        n = len(grid[0])
        
        # Initialize a 2D array to store the minimum sum for each cell
        dp = [[0] * n for _ in range(m)]
        
        # Set the first element of dp as the value of the first element in grid
        dp[0][0] = grid[0][0]
        
        # Fill the first row of dp
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        # Fill the first column of dp
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill up the rest of dp
        for i in range(1, m):
            for j in range(1, n):
                # The minimum sum for each cell is the value of the cell plus the minimum sum of its top or left neighbor
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # Return the minimum sum for the last cell in dp
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Expected: 7
    print(s.minPathSum([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: 12