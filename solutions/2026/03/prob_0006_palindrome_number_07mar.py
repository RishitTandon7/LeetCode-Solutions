def isPalindrome(x: int) -> bool:
    """
    Approach: We can convert the integer into a string and compare it with its reverse.
    Time Complexity: O(n), where n is the number of digits in the integer.
    Space Complexity: O(n), as we need to store the string representation of the integer.
    """
    # Convert the integer into a string
    str_x = str(x)
    
    # Compare the string with its reverse
    return str_x == str_x[::-1]

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(isPalindrome(121))  # Expected: True
    print(isPalindrome(123))  # Expected: False