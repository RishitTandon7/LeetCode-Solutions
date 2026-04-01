from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[Optional[int]]:
        """
        Approach: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Create a hash table to store the numbers and their indices. 
        Iterate through the list of numbers, for each number calculate its complement (target - num). 
        If the complement is found in the hash table, return the index of the complement and the current number.
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []