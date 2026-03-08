from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach: Two pointers, one at the start and one at the end of the array.
        We calculate the area between the two pointers and move the pointer with the smaller height towards the other pointer.
        If the area is greater than the max_area, we update max_area.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # calculate the area
            area = min(height[left], height[right]) * (right - left)

            # update max_area if necessary
            if area > max_area:
                max_area = area

            # move the pointer with the smaller height
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