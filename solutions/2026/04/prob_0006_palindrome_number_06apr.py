def isPalindrome(x: int) -> bool:
    """
    Approach: Convert integer to string, compare with reverse
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if x < 0:  # Negative numbers cannot be palindrome
        return False
    str_x = str(x)  # Convert integer to string
    return str_x == str_x[::-1]  # Compare with reverse

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(isPalindrome(12321))  # Expected: True
    print(isPalindrome(-121))   # Expected: False