from typing import List, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[Tuple[int]]:
        """
        Approach: Sort the array and use two pointers to find the triplets.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        # Step 1: Sort the input array
        nums.sort()
        
        # Initialize an empty list to store the result
        result = []
        
        # Iterate over the array
        for i in range(len(nums) - 2):
            # Skip the same result
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers, one at the start and one at the end of the remaining array
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                # Calculate the current sum
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If the current sum is zero, we have found a valid triplet
                if current_sum == 0:
                    result.append((nums[i], nums[left], nums[right]))
                    
                    # Move the pointers to find the next valid triplet
                    left += 1
                    right -= 1
                    
                    # Skip the same result
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                
                # If the current sum is less than zero, move the left pointer to increase the sum
                elif current_sum < 0:
                    left += 1
                
                # If the current sum is greater than zero, move the right pointer to decrease the sum
                else:
                    right -= 1
        
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))  # Expected: [(-1, -1, 2), (-1, 0, 1)]
    print(s.threeSum([0,1,1]))  # Expected: []
    print(s.threeSum([0,0,0]))  # Expected: [(0, 0, 0)]