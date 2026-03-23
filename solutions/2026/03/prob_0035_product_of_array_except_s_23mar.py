from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach: We use two passes to calculate the product of all numbers except self.
        
        First pass: Calculate the running product from left to right.
        Second pass: Calculate the running product from right to left and multiply it with the first pass result.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize output array
        output = [1] * len(nums)

        # First pass: Calculate the running product from left to right
        left_product = 1
        for i in range(len(nums)):
            output[i] *= left_product
            left_product *= nums[i]

        # Second pass: Calculate the running product from right to left and multiply it with the first pass result
        right_product = 1
        for i in reversed(range(len(nums))):
            output[i] *= right_product
            right_product *= nums[i]

        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))  # Expected: [24,12,8,6]
    print(s.productExceptSelf([1,1,1,1]))  # Expected: [1,1,1,1]
    print(s.productExceptSelf([2,3,4,5]))  # Expected: [60,40,30,24]