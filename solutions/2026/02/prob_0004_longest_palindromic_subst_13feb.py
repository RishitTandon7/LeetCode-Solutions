class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: 
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        
        This function works by expanding around each character in the string.
        It checks if a substring is a palindrome and keeps track of the longest one found so far.
        """
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # odd length palindrome
            odd_palindrome = expand_around_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # even length palindrome
            even_palindrome = expand_around_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest