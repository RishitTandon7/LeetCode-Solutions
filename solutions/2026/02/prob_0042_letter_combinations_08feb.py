from typing import List, Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Approach: Recursive backtracking with string manipulation
        Time Complexity: O(4^n), where n is the number of digits
        Space Complexity: O(n), for the recursion stack and result list
        """
        
        # Define the phone keypad mapping
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        # Base case: if the input string is empty, return an empty list
        if not digits:
            return []
        
        # Recursive case: generate combinations for each digit and combine them
        def backtrack(combination, next_digits):
            # If there are no more digits to process, add the current combination to the result
            if len(next_digits) == 0:
                output.append(combination)
            else:
                # Get the possible letters for the next digit
                for letter in keypad[next_digits[0]]:
                    # Recursively call backtrack with the updated combination and reduced number of digits
                    backtrack(combination + letter, next_digits[1:])
        
        # Initialize the result list and process each digit
        output = []
        for digit in digits:
            backtrack("", digit)
        
        return output

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))  # Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']