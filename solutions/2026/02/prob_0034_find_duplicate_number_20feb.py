from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Approach: Floyd's Tortoise and Hare algorithm, also known as the "Cycle Detection" algorithm.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Detecting the cycle
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Finding the start of the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))  # Expected: 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))  # Expected: 3
    print(s.findDuplicate([1, 1, 2]))  # Expected: 1