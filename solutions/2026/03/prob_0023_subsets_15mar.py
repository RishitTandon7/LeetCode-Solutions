from typing import List, Optional

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        
        The idea is to start with an empty subset and then add each number from the input list.
        We use a backtracking approach to generate all possible subsets.
        """
        # Initialize an empty list to store the result
        result = []
        
        # Define a helper function for backtracking
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path[:])
            
            # Iterate over each number in the input list starting from the start index
            for i in range(start, len(nums)):
                # Add the current number to the path and recursively call the backtrack function
                path.append(nums[i])
                backtrack(i + 1, path)
                # Remove the last added number from the path (backtracking)
                path.pop()
        
        # Call the backtrack function with an empty start index and an empty path
        backtrack(0, [])
        
        # Return the result
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[], [0]]