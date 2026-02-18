class Solution:
    def validParentheses(self, s: str) -> bool:
        """
        Approach: We use a stack to keep track of the opening parentheses.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Create a dictionary to map closing parentheses to their corresponding opening ones
        pairs = {")": "(", "}": "{", "]": "["}
        
        # Initialize an empty stack
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char in pairs.values():
                stack.append(char)
            # If the character is a closing parenthesis
            elif char in pairs.keys():
                # If the stack is empty or the top of the stack does not match the current closing parenthesis, return False
                if len(stack) == 0 or stack.pop() != pairs[char]:
                    return False
        
        # After iterating over the entire string, if the stack is empty, it means all parentheses were properly matched and we can return True
        # Otherwise, we return False because there are unmatched opening parentheses left in the stack
        return len(stack) == 0