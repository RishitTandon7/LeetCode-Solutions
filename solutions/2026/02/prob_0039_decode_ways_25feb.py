from typing import List

class Solution:
    def decodeWays(self, s: str) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.decodeWays("12"))  # Expected: 2
    print(s.decodeWays("226"))  # Expected: 3
    print(s.decodeWays("0"))  # Expected: 0
    print(s.decodeWays("10"))  # Expected: 1
    print(s.decodeWays("1023"))  # Expected: 1