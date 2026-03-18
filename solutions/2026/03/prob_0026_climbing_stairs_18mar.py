class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We create a list dp where dp[i] represents the number of ways to reach the ith stair.
        The base case is when i = 0 or i = 1, in which case there's only one way to reach that stair (by not moving at all or by taking one step).
        For each stair from the second to the nth, we can either take one step from the previous stair or two steps from the stair before that.
        So, dp[i] is the sum of dp[i-1] and dp[i-2].
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n <= 2:
            return n
        self.dp = [0]*(n+1)
        self.dp[1] = 1
        self.dp[2] = 2
        for i in range(3, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))  # Expected: 5
    print(s.climbStairs(10))  # Expected: 89