from typing import List, Optional

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[Optional[int]]:
        """
        Approach: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Create a hash table to store the indices of the elements in the list.
        Iterate over the list and for each element, check if its complement (target - element) is in the hash table.
        If it is, return the current index and the index of the complement. Otherwise, continue to the next element.
        
        :param numbers: A list of integers
        :type numbers: List[int]
        :param target: The target sum
        :type target: int
        :return: A list containing the indices of the two elements that add up to the target
        :rtype: List[Optional[int]]
        """
        num_dict = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        
        # If no solution is found
        return None

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(s.twoSum([3, 2, 4], 6))  # Expected: [1, 2]