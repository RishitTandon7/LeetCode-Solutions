from typing import List, Optional

class Solution:
    def medianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: Merge the two sorted arrays and find the middle element.
        Time Complexity: O(n + m), where n and m are the lengths of the two arrays.
        Space Complexity: O(n + m), where n and m are the lengths of the two arrays.
        """
        # Merge the two sorted arrays into one
        merged = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        # Append the remaining elements, if any
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Find the middle element
        n = len(merged)
        if n % 2 == 0:
            # If the length is even, the median is the average of the two middle elements
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            # If the length is odd, the median is the middle element
            return merged[n // 2]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.medianSortedArrays([1, 3], [2]))  # Expected: 2
    print(s.medianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5
    print(s.medianSortedArrays([1, 3, 5], [2, 4]))  # Expected: 3