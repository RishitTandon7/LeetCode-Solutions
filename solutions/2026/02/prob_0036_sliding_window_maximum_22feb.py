from typing import List, Optional

class Solution:
    def maxSlidingMaxQueue(self, nums: List[int]) -> List[int]:
        """
        Approach: We use a deque to store the indices of the elements in the input list. 
        We always remove the front of the deque if the element at the front is smaller than the current element. 
        We also remove the back of the deque if the back element is smaller than the current maximum. 
        We use a dictionary to store the index of the maximum element for each element in the deque. 
        When we find a new maximum, we update the index of the maximum element in the dictionary. 
        Finally, we return the elements in the deque in the order they were added.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Initialize the deque and the dictionary
        dq = []
        max_dict = {}
        
        # Initialize the result list
        result = []
        
        # Iterate over the input list
        for i, num in enumerate(nums):
            # Remove the front of the deque if the element at the front is smaller than the current element
            while dq and nums[dq[-1]] < num:
                max_dict.pop(dq.pop(), None)
            
            # Add the current element to the deque
            dq.append(i)
            
            # Update the index of the maximum element in the dictionary
            max_dict[num] = i
            
            # Remove the back of the deque if the back element is smaller than the current maximum
            while dq and nums[dq[0]] < num:
                dq.popleft()
            
            # Add the current maximum to the result list
            result.append(max_dict[num])
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingMaxQueue([1,3,-1,-3,5,3,6,7]))  # Expected: [3,3,5,5,6,7]
    print(s.maxSlidingMaxQueue([1,2]) )  # Expected: [1,1]
    print(s.maxSlidingMaxQueue([3,1,5,6,4]) )  # Expected: [3,3,5,5,6]