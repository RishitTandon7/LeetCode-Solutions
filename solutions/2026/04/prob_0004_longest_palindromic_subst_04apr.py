from typing import List, Optional

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: Manacher's Algorithm with a twist to handle odd length palindromes.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Preprocess the string
        T = '#'.join('^{}$'.format(s))
        n = len(T)

        # Initialize P and C arrays
        P = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            # Find rightmost non-central palindrome
            if i < R:
                left = 2 * C - i
                right = min(R + R - i, n - 1)
                P[i] = min(P[left], R - i)

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i is longer than the previous longest palindrome
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find the length of the longest palindrome in the original string
        maxLen = 0
        for i in range(n):
            if T[i] == s[0]:
                start, end = i - maxLen, i + maxLen
                while start >= 1 and end < n - 1 and s[(start-1)//2] == s[end//2]:
                    start -= 1
                    end += 1
                if start > 0:
                    maxLen = (end - start) // 2

        return s[:maxLen+1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))  # Expected: "bab"
    print(s.longestPalindrome("cbbd"))   # Expected: "bb"