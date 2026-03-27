from typing import List, Optional

class Solution:
    def decodeWays(self, s: str) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        The idea is to use dynamic programming to build up a table where dp[i] represents the number of ways to decode the string from index 0 to i.
        We can either take the last digit as part of the current way or start a new way. If we take the last digit, we need to make sure that the remaining digits are valid (i.e., between 10 and 26).
        """
        
        # Base case: if the string is empty, there's only one way to decode it
        if not s:
            return 1
        
        # Initialize a table to store the number of ways to decode the string from index i to j
        dp = [0] * (len(s) + 1)
        
        # There's only one way to decode an empty string
        dp[0] = 1
        
        # For each digit in the string
        for i in range(1, len(s) + 1):
            # If the current digit is not zero, we can take it as part of the current way
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # If the last two digits are between 10 and 26, we can start a new way with these two digits
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        # The number of ways to decode the entire string is stored in the last element of the table
        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.decodeWays("12"))  # Expected: 2
    print(s.decodeWays("226"))  # Expected: 3
    print(s.decodeWays("0"))  # Expected: 1