from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: We use a sliding window approach with two pointers and a set to keep track of unique characters in the current substring.
        
        Time Complexity: O(n), where n is the length of the input string. This is because we are scanning through the string once.

        Space Complexity: O(min(n, m)), where m is the size of the character set. In the worst case, all characters in the string are unique, so the size of the set will be equal to the length of the string.
        """
        # Initialize variables
        max_length = 0
        char_set = set()
        left = 0

        # Iterate over the string
        for right in range(len(s)):
            # While the character at the right pointer is in the set, remove the character at the left pointer from the set and move the left pointer to the right.
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the character at the right pointer to the set
            char_set.add(s[right])

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length