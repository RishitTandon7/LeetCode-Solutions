class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We create a 2D array dp where dp[i][j] represents the number of unique paths from (0,0) to (i,j).
        The base case is when i or j is 0, there's only one way to reach that point (by always moving right or up respectively).
        For other points, we can move either up or right and add the number of ways for the previous two points.
        
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        # Create a 2D array dp with zeros
        dp = [[0]*n for _ in range(m)]
        
        # Initialize base cases
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill up the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths is stored in dp[m-1][n-1]
        return dp[m-1][n-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))  # Expected: 28
    print(s.uniquePaths(10, 20))  # Expected: 500