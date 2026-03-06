def reverseInteger(x: int) -> int:
    """
    Approach: This function uses a simple mathematical approach to reverse the integer.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Convert the integer to a string to easily reverse it
    sign = -1 if x < 0 else 1
    x *= sign

    # Reverse the string
    reversed_x = str(x)[::-1]

    # Convert the reversed string back to an integer
    reversed_x = int(reversed_x)

    # Apply the original sign back to the result
    reversed_x *= sign

    # Check if the reversed integer is within the 32-bit signed integer range
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0

    return reversed_x