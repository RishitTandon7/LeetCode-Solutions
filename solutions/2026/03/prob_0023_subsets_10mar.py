from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Recursive backtracking to generate all subsets.
        Time Complexity: O(2^n) where n is the length of the input list.
        Space Complexity: O(2^n) due to the recursive call stack and the storage of all subsets.
        """
        # Base case: if the input list is empty, return a list containing an empty list
        if not nums:
            return [[]]

        # Recursive case: get all subsets of the input list excluding the first element
        subsets_excluding_first = self.subsets(nums[1:])

        # Recursive case: get all subsets of the input list including the first element
        subsets_including_first = [[nums[0]] + subset for subset in subsets_excluding_first]

        # Combine the results of the two recursive cases
        return subsets_excluding_first + subsets_including_first

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))  # Expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(s.subsets([0]))  # Expected: [[], [0]]
    print(s.subsets([]))  # Expected: []