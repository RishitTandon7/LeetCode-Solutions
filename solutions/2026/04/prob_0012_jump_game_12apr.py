from typing import List, Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Approach: This problem can be solved using dynamic programming.
        We initialize a list dp where dp[i] represents the maximum number of steps we can take from index i.
        The base case is when we are at the last index, so dp[-1] = 0.
        Then for each index i, if we have already visited it before (dp[i] > 0), then we update dp[j] to be the maximum of its current value and 1 + dp[i], where j is the next index that we can jump to.
        Finally, we return the last element in dp which represents the minimum number of jumps required.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n <= 1:
            return 0
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            else:
                max_reach = nums[i] + min(dp[:i])
                dp[i] = float('inf')
                for j in range(i-1, -1, -1):
                    if j < 0 or nums[j] + i > max_reach:
                        break
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))  # Expected: 2
    print(s.jump([2,3,0,1,4]))  # Expected: 2