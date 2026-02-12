from typing import List, Optional
import heapq

class Solution:
    def medianFinder(self, nums1: List[int], nums2: List[int]) -> Optional[float]:
        """
        Approach: We will use two heaps to solve this problem. The smaller heap will store the smaller half of the elements from both arrays, and the larger heap will store the larger half of the elements from both arrays.
        
        Time Complexity: O(log(min(m,n))) where m and n are the sizes of nums1 and nums2 respectively.
        
        Space Complexity: O(1)
        """
        # Initialize two heaps
        smaller = []  # stores the smaller half of the elements from both arrays
        larger = []  # stores the larger half of the elements from both arrays
        
        # Add all elements from both arrays to the heaps
        for num in nums1:
            heapq.heappush(smaller, -num)
        for num in nums2:
            heapq.heappush(larger, num)
        
        # Balance the heaps if necessary
        while len(smaller) > len(larger) + 1:
            heapq.heappush(larger, -heapq.heappop(smaller))
        while len(larger) > len(smaller) + 1:
            heapq.heappush(smaller, -heapq.heappop(larger))
        
        # Calculate the median
        if len(smaller) == len(larger):
            return (-smaller[0] + larger[0]) / 2
        elif len(smaller) > len(larger):
            return -smaller[0]
        else:
            return larger[0]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.medianFinder([1, 3], [2]))  # Expected: 2
    print(s.medianFinder([1, 2], [3, 4]))  # Expected: 2.5