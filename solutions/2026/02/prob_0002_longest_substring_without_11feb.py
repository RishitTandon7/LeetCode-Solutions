from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: We use a sliding window approach with two pointers to track the start and end of the current substring.
        Time Complexity: O(n), where n is the length of the string. This is because we are scanning through the string once.
        Space Complexity: O(min(n, m)), where m is the size of the character set. In the worst case scenario, we need to store all characters in the hash map.

        """
        # Initialize variables
        max_length = 0
        char_index_map = {}

        # Initialize the window boundaries
        left = 0

        # Iterate over each character in the string
        for right, char in enumerate(s):
            # If the character is already in our window, we need to slide the window to the right of the previous occurrence
            if char in char_index_map and char_index_map[char] >= left:
                left = max(char_index_map[char] + 1, left)

            # Update the index of the current character in the hash map
            char_index_map[char] = right

            # Update our maximum length
            max_length = max(max_length, right - left + 1)

        return max_length