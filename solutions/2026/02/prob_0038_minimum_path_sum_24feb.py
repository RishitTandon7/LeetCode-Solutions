from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        # Initialize the first element of dp
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill up the dp table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Expected: 7
    print(s.minPathSum([[1,2,3],[4,5,6],[7,8,9]]))  # Expected: 12