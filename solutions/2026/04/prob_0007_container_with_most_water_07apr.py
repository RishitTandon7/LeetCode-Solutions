from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two pointers technique with two lines of code.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize variables
        left = 0
        right = len(height) - 1
        max_area = 0

        # Loop until the two pointers meet
        while left < right:
            # Calculate the area between the two lines
            current_area = min(height[left], height[right]) * (right - left)
            
            # Update the maximum area if necessary
            max_area = max(max_area, current_area)

            # Move the pointer of the shorter line towards the other pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(s.maxArea([1,1]))  # Expected: 1
    print(s.maxArea([4,3,2,1,4]))  # Expected: 16