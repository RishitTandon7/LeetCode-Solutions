from typing import List, Optional

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        """
        Approach: 
            We use a modified binary search algorithm to find the index of the target element in the sorted array.
            The key difference between this approach and regular binary search is that we can move forward or backward depending on whether the target element is greater than or less than the middle element.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.binarySearch([1, 3, 5, 7, 9], 5))  # Expected: 2
    print(s.binarySearch([1, 3, 5, 7, 9], 6))  # Expected: -1