from typing import List, Optional
import itertools

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Approach: 
        Time Complexity: O(4^n / n^(3/2)) due to backtracking and generating all possible combinations of parentheses.
        Space Complexity: O(4^n / n^(3/2)) as well due to the recursive call stack.

        This problem is solved using a combination of recursion, backtracking, and itertools. The idea is to generate all possible combinations of opening and closing parentheses, then filter out invalid ones.
        """
        
        def backtrack(open_count: int, close_count: int, current: str) -> List[str]:
            # Base case: when the length of the current string equals 2n
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Recursive case: generate all possible combinations of opening and closing parentheses
            for i in range(open_count, close_count + 1):
                backtrack(i + 1, min(close_count, open_count - (i - open_count)), current + '(')
                if open_count != close_count:
                    backtrack(open_count, i - open_count, current + ')')
        
        result = []
        backtrack(0, 0, '')
        return result

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))  # Expected: ['((()))', '(()())', '(())()', '()(())', '()()()' ]