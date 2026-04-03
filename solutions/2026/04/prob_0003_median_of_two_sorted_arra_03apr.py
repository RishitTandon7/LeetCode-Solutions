from typing import List, Optional

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Approach: 
            We will use a two-pointer technique to traverse both arrays simultaneously.
            The idea is to keep track of the smaller element and the larger element at each step.
            If one array is longer than the other, we can extend the shorter array with zeros.
        
        Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively.
        Space Complexity: O(1)
        """
        
        # Make sure that nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Calculate the total length of both arrays
        total_length = len(nums1) + len(nums2)
        
        # Initialize two pointers, one for each array
        left, right = 0, (total_length - 1) // 2
        
        while True:
            # Calculate the partition point for nums1
            i = (left + right) // 2
            
            # Calculate the corresponding partition point for nums2
            j = total_length // 2 - i - 2
            
            # Calculate the values at the partition points
            nums1_left = nums1[i] if i < len(nums1) else float('-infinity')
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
            nums2_left = nums2[j] if j < len(nums2) else float('-infinity')
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')
            
            # Check if the partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # If the total length is even, return the average of the two middle numbers
                if total_length % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                # If the total length is odd, return the middle number
                else:
                    return max(nums1_left, nums2_left)
            # If the partition is not correct, adjust the pointers and repeat
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))  # Expected: 2.0
    print(s.findMedianSortedArrays([1,2], [3,4]))  # Expected: 2.5