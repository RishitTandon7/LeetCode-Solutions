from typing import List, Optional
from collections import deque

class Solution:
    def validParentheses(self, s: str) -> bool:
        """
        Approach: We use a stack to keep track of the opening parentheses.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Create a dictionary to map closing brackets to their corresponding opening ones
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        # Initialize an empty stack
        stack = deque()
        
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing parenthesis, check if the stack is empty or its top element does not match with the current closing parenthesis
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
        
        # After iterating over all characters, if the stack is empty, it means every opening parenthesis has been matched with a corresponding closing one
        return not stack

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.validParentheses("()"))  # Expected: True
    print(s.validParentheses("()[]{}"))  # Expected: True
    print(s.validParentheses("(]"))  # Expected: False
    print(s.validParentheses("([)]"))  # Expected: False
    print(s.validParentheses("{[]}"))  # Expected: True