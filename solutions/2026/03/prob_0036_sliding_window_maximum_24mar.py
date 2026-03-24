from typing import List, Optional
import heapq

class Solution:
    def maxSlidingModule(self, nums: List[int]) -> List[int]:
        """
        Approach: We use a deque to store indices of elements in descending order.
        Time Complexity: O(n log n) due to the heap operations.
        Space Complexity: O(n) for storing the indices and the result list.
        """
        # Initialize the result list
        result = []
        
        # Initialize the deque to store indices
        dq = []
        
        # Iterate over the input list
        for i, num in enumerate(nums):
            # Remove elements from the back of the deque that are smaller than the current number
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            # Add the current index to the front of the deque
            dq.append(i)
            
            # If the first element in the deque is out of the current window, remove it
            if dq[0] == i - len(nums):
                dq.pop(0)
            
            # If the current window size is greater than 1, add its maximum value to the result list
            if i >= len(nums) - 1:
                result.append(nums[dq[0]])
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingModule([1,3,-1,-3,5,3,6,7]))  # Expected: [3,3,5,5,6]
    print(s.maxSlidingModule([1,2]) )  # Expected: [1]